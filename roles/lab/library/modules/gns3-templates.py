#!/usr/bin/env python
ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---

"""

EXAMPLES = """

"""

RETURN = """

"""

import traceback
from ansible.module_utils.basic import AnsibleModule, missing_required_lib

GNS3FY_IMP_ERR = None
try:
    from gns3fy import Gns3Connector

    HAS_GNS3FY = True
except Exception:
    HAS_GNS3FY = False
    GNS3FY_IMP_ERR = traceback.format_exc()


def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(type="str", required=True),
            port=dict(type="int", default=3080),
            user=dict(type="str", default=None),
            password=dict(type="str", default=None, no_log=True),
            get_images=dict(type="str", default=None),
            get_compute_ports=dict(type="bool", default=False),
        )
    )
    result = dict(changed=False)
    if not HAS_GNS3FY:
        module.fail_json(msg=missing_required_lib("gns3fy"), exception=GNS3FY_IMP_ERR)

    server_url = module.params["url"]
    server_port = module.params["port"]
    server_user = module.params["user"]
    server_password = module.params["password"]
    get_images = module.params["get_images"]
    get_compute_ports = module.params["get_compute_ports"]
