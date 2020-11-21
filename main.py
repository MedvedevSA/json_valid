import json
import os
from jsonschema import validate
from jsonschema import Draft3Validator

cwd = os.getcwd()
event_path = cwd + "\\event"
schema_path = cwd + "\\schema"

tree = os.walk(cwd)
folder = []

for i in os.walk(cwd):
     folder.append(i)

file_list = []
for address, dirs, files in folder:
    for file in files:
        file_list.append( address + '\\'+file)

is_open = 0


for file_schema in file_list:
    if file_schema.find(".schema") > 0:
        with open(file_schema) as f:
            cur_schema = json.load(f)
            for file_json in file_list:
                if file_json.find(".json") > 0:
                    with open(file_json) as f:
                        cur_json = json.load(f)

                        instance = cur_json
                        v = Draft3Validator(cur_schema)
                        errors = sorted(v.iter_errors(instance), key=lambda e: e.path)
                        for error in errors:
                            print(error.message)
                        
                        """
                        print(file_schema,"---->",file_json)
                        print(Draft3Validator(cur_schema).is_valid(cur_json))
                        """
            break
            #print (json.dumps(cur_schema, indent = 2))
        

        print("--------------------------------------")
            #print (json.dumps(cur_json, indent = 2))
            

print("")

