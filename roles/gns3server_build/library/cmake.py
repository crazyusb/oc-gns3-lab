#!/usr/bin/python
ANSIBLE_METADATA = {
    "metadata_version": "0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: cmake
description:
    - Build a project using CMake.
author:
    - Benoit Fredet (@Crazyusb)
options:
  binary_dir:
    description: Destination for binaries.
    required: true
  source_dir:
    description: |
      Location of C(CMakeLists.txt). This is required the first time a project
      is built, or use it to tell CMake to regenerate the build files.
    required: false
  executable:
    description: Path to the C(cmake) executable.
    required: false
"""
EXAMPLES = """
# Build a binary.
- cmake:
    source_dir: /path/to/project
    binary_dir: /path/to/broject/build
""" 

# Import ansible module boilerplate as stated here "https://ansible-docs.readthedocs.io/zh/stable-2.0/rst/developing_modules.html#common-module-boilerplate"
from ansible.module_utils.basic import *

from glob import glob
from os.path import abspath
from subprocess import Popen
from subprocess import PIPE

# Define args passed via playbook 

def main():
    module = AnsibleModule(
        argument_spec=dict(
           binary_dir=dict(type='str', required=True),
           source_dir=dict(type='str', default=None),
           creates=dict(type='str', default=""),
           executable=dict(type='str', default="cmake"),
        )
    )

    def cmake(args):
        # Exec Cmake
        # Any output to STDOUT or STDERR must be captured.
        args = [module.params["executable"]] + list(args)
        process = Popen(args, stdout=PIPE, stderr=PIPE, cwd=binary)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            module.fail_json(msg=stderr, stdout=stdout, rc=process.returncode)
        return

    def config():
        # Execute the CMake config step.
        args = []
        source = abspath(module.params["source_dir"])
        args.append(source)
        cmake(args)
        return

    def build():
        # Execute the CMake build step. 
        args = ["--build", binary]
        cmake(args)
        return

    required = not glob(module.params["creates"])
    if module.check_mode:
        module.exit_json(changed=required)  # calls exit(0)
    if required:
        binary = abspath(module.params["binary_dir"])
        if module.params["source_dir"]:
            config()
        build()
    module.exit_json(changed=required, rc=0, **module.params)  # calls exit(0)


# Make the module executable.

if __name__ == "__main__":
    raise SystemExit(main())