#!/usr/bin/python
from ansible.module_utils.basic import *
import requests

def main():
    module = AnsibleModule(
        argument_spec=dict(
           url=dict(type='str', required=True),
           port=dict(type='int', default=3080),
           api=dict(type="str", default="v2"),
           page=dict(type="str", required=True),
           user=dict(type="str", default=None),
           password=dict(type="str", default=None, no_log=True),
        )
    )
    result = dict(changed=False)

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