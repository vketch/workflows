import json
import pickle

WORKFLOW_FILE = "gardenstate_mls_workflow_.py"
#WORKFLOW_FILE = "test_dict.py"

 # def str2json( str ):
 #     js = json.loads(str)
 #     print( json.dump(js) )

# with open(WORKFLOW_FILE, 'rb') as handle:
#   b = pickle.loads(handle.read())
#print(b)

fw_dic ={}
with open(WORKFLOW_FILE, 'r') as infile:
     fw_dic = eval(infile.read())
#print( fw_dic )

#print(fw_dic['workflow'])

fw_js = json.loads(fw_dic['workflow'])

print(json.dumps(fw_js))
print(fw_js["actions"][0]['mapping'])
mp_js = json.loads(fw_js["actions"][0]['mapping'])
print(mp_js ["state"])

#action_str = json.loads(fw_js.get("actions"))
#print(action_str)

#map_js = json.loads(fw_dic['workflow'])
#print(fw_js.)
#str2json(forkflow)

