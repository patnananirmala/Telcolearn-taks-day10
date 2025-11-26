
#list all services port
'''import yaml

with open("docker_compose.yaml") as f:
    data = yaml.safe_load(f)

for name, service in data["services"].items():
    ports = []

    for env in service.get("environment", []):
        if "=" in env:
            key, val = env.split("=", 1)

            # only vars ending with _PORT
            if key.endswith("_PORT") and val.isdigit():
                ports.append(val)

    print(f"{name} -> Ports: {list(set(ports))}")'''

import yaml

with open("docker_compose.yaml") as f:
    data = yaml.safe_load(f)

for name, service in data["services"].items():
    ports = []
    seen = set()   # to track unique ports

    for env in service.get("environment", []):
        if "=" in env:
            key, val = env.split("=", 1)

            if key.endswith("_PORT") and val.isdigit():
                if val not in seen:   # keep order
                    ports.append(val)
                    seen.add(val)

    print(f"{name} -> Ports: {ports}")




