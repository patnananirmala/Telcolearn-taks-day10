# services_ipaddress.py
#gives the services ip address in json file
'''import yaml
from pathlib import Path

def load_compose(path="docker_compose.yaml"):
    text = Path(path).read_text(encoding="utf-8")
    return yaml.safe_load(text)

def extract_services(compose):
    services = compose.get("services", {})
    out = {}
    for name, svc in services.items():
        info = {}
        # depends_on (may be missing)
        info["depends_on"] = svc.get("depends_on") or []
        # find ipv4_address inside networks (if any)
        info["ipv4_addresses"] = []
        svc_networks = svc.get("networks", {}) or {}
        # svc_networks could be list or dict; handle dict case (most common)
        if isinstance(svc_networks, dict):
            for net_name, net_cfg in svc_networks.items():
                if isinstance(net_cfg, dict):
                    ip = net_cfg.get("ipv4_address")
                    if ip:
                        info["ipv4_addresses"].append({"network": net_name, "ipv4_address": ip})
        out[name] = info
    return out

def print_report(services_info):
    print("Service\t\tIPv4 Address(es)\t\tDepends On")
    print("-"*80)
    for svc, info in services_info.items():
        ips = ", ".join([f"{i['ipv4_address']}({i['network']})" for i in info["ipv4_addresses"]]) or "None"
        deps = ", ".join(info["depends_on"]) or "None"
        print(f"{svc:15}\t{ips:30}\t{deps}")

if __name__ == "__main__":
    compose = load_compose("docker_compose.yaml")
    services_info = extract_services(compose)
    print_report(services_info)
def load_compose_from_string(yaml_text):
    return yaml.safe_load(yaml_text)'''

import yaml

with open("docker_compose.yaml") as f:
    data = yaml.safe_load(f)

for name, service in data["services"].items():
    ip = list(service.get("networks", {}).values())[0].get("ipv4_address")
    deps = service.get("depends_on", [])
    print(f"{name} -> IP: {ip}, Depends On: {deps}")


