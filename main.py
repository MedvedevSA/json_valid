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


for file in file_list:
    if file.find(".schema") > 0:
        with open(file) as f:
            cur_schema = json.load(f)
            print (json.dumps(cur_schema, indent = 2))
        break


            #print (json.dumps(cur_json, indent = 2))
for file in file_list:
    if file.find(".json") > 0:
        with open(file) as f:
            cur_json = json.load(f)
            print(Draft3Validator(cur_schema).is_valid(cur_json))
        

print("")

