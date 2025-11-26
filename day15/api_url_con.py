
#convert yaml to json
import yaml
import json
with open(r"C:\Users\nirma\Downloads\TS24549_ETC_Configuration.yaml") as f:
    data=yaml.safe_load(f)
json_data=json.dumps(data,indent=2)
print(json_data)

##convert json to yaml
import json,yaml
with open(r"C:\Users\nirma\Downloads\sample2 (1).json") as f:
    j=json.load(f)
yaml_out=yaml.dump(j,default_flow_style=False)
print(yaml_out)