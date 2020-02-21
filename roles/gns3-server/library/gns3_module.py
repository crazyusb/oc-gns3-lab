#!/usr/bin/python

ANSIBLE_METADATA = {
    "metadata_version": "0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: gns3_module
short_description: Module that retrieves the version of a GNS3 server
description:
    - Module that retrieves the version of a GNS3 server
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
    api:
        description:
            - Version of the API
        type: 
        default: v2
    page:
        description:
             - Page where information are stored
        default: version
        type: str
"""

EXAMPLES = """
# Retrieves all the  information from the computes of GNS3 server
- name: Retrieve all the facts of a GNS3 server computes
  gns3_get_version:
    url: http://localhost
    port: 3080
    page: version
  register: gns3_version
- debug: var=gns3_version
"""

RETURN = """
verision:
    description: Get server version
    type: str
"""

# Import ansible module boilerplate as stated here "https://ansible-docs.readthedocs.io/zh/stable-2.0/rst/developing_modules.html#common-module-boilerplate"
from ansible.module_utils.basic import *
# Import requests lib for Rest call
import requests

# Define Ansible module args
def main():
    module = AnsibleModule(
        argument_spec=dict(
           url=dict(type='str', required=True),
           port=dict(type='int', default=3080),
           api=dict(type="str", default="v2"),
           page=dict(type="str", default="version"),
        )
    )
    result = dict(changed=False)

# Put ansible args in variable for simplified use in call api

    server_url = module.params["url"]
    server_port = module.params["port"]
    server_api = module.params["api"]
    server_page = module.params["page"]

    try:
        call_api = requests.get(url=f"{server_url}:{server_port}/{server_api}/{server_page}")
        facts = call_api.json()
        result["facts"] = facts
        module.exit_json(**result)

    except Exception as err:
        module.fail_json(msg=str(err), **result)


if __name__ == '__main__':
    main()