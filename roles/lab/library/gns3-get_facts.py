#!/usr/bin/env python3
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

    try:
        # Create server session
        server = Gns3Connector(
            url=f"{server_url}:{server_port}", user=server_user, cred=server_password
        )

        computes = server.get_computes()
        for compute in computes:

            # Images
            if get_images:
                compute["images"] = dict()

                if get_images == "all":
                    for emulator in compute["capabilities"]["node_types"]:
                        try:
                            compute["images"][emulator] = server.get_compute_images(
                                emulator=emulator, compute_id=compute["compute_id"]
                            )
                        except Exception as err:
                            if "404" in str(err):
                                # Contine if no image dir is set for that emulator
                                continue
                else:
                    compute["images"][get_images] = server.get_compute_images(
                        emulator=get_images, compute_id=compute["compute_id"]
                    )

            # Compute ports
            if get_compute_ports:
                compute["compute_ports"] = server.get_compute_ports(
                    compute_id=compute["compute_id"]
                )

        result["facts"] = computes
        module.exit_json(**result)
    except Exception as err:
        module.fail_json(msg=str(err), **result)


if __name__ == "__main__":
    main()