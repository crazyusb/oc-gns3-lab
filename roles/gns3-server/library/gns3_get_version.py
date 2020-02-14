#!/usr/bin/env python3

ANSIBLE_METADATA = {
    "metadata_version": "0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: gns3_get_version
short_description: Module that retrieves the version of a GNS3 server
version_added: '2.8'
description:
    - Module that retrieves the compute(s) information of a GNS3 server
requirements: [ gns3fy ]
author:
    - Benoit Fredet (@Crazyusb)
options:
    url:
        description:
            - URL target of the GNS3 server
        required: true
        type: str
    port:
        description:
            - TCP port to connect to server REST API
        type: int
        default: 3080
    user:
        description:
            - User to connect to GNS3 server
        type: str
    password:
        description:
            - Password to connect to GNS3 server
        type: str
"""

EXAMPLES = """
# Retrieves all the  information from the computes of GNS3 server
- name: Retrieve all the facts of a GNS3 server computes
  gns3_get_version:
    url: http://localhost
    port: 
  register: gns3_version

- debug: var=gns3_version
"""

RETURN = """
verision:
    description: Get server version
    type: str
"""


#Import ansible module
import traceback
from ansible.module_utils.basic import AnsibleModule, missing_required_lib

#Check if gns3fy lib is present
GNS3FY_Set = None
try:
    from gns3fy import Gns3Connector
    GNS3FY_install = True
except Exception:
    GNS3FY_install = False
    GNS3FY_Set = traceback.format_exc()

# Define entry from ansible module
def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(type="str", required=True),
            port=dict(type="int", default=3080),
            user=dict(type="str", default=None),
            password=dict(type="str", default=None, no_log=True),
        )
    )

    result = dict(changed=False)

# Return error if gns3fy not installed
    if not GNS3FY_install:
        module.fail_json(msg=missing_required_lib("gns3fy"), exception=GNS3FY_Set)

# Link ansible variable from module

    server_url = module.params["url"]
    server_port = module.params["port"]
    server_user = module.params["user"]
    server_password = module.params["password"]

    try:
        # Create server session
        server = Gns3Connector(
            url=f"{server_url}:{server_port}", user=server_user, cred=server_password
        )
        # Get gns3 server version
        version = server.get_version()
        result["facts"] = version
        module.exit_json(**result)
    except Exception as err:
        module.fail_json(msg=str(err), **result)


if __name__ == "__main__":
    main()