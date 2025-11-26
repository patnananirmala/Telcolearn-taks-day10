import yaml
import json
with open("docker_compose.yaml") as f:
    data=yaml.safe_load(f)
#print(data["services"]["oai-amf"])
service=data["services"]["oai-amf"]
list=service.get("environment",[])
dict={}
for i in list:
    if "=" in i:
        key,value=i.split("=",1)
        dict[key]=value
print("MCC =",dict.get("MCC"))
data=yaml.safe_load(open("docker_compose.yaml"))
json_data=json.dumps(data,indent=2)
print(json_data)