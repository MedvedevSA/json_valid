import json
import os
from jsonschema import validate
from jsonschema import Draft3Validator

cwd = os.getcwd()                           #считываем текущую директорию
event_path = cwd + "\\event"                
schema_path = cwd + "\\schema"

tree = os.walk(cwd)                         #читаем все что лежит рядом и глубже внутри, сохрянияем в tree 
folder = []

for i in os.walk(cwd):
     folder.append(i)                       #создаем список доступных папок

file_list = []
for address, dirs, files in folder:
    for file in files:
        file_list.append( address + '\\'+file)          #Создаем список файлов для всех папок, все в одной куче




for file_schema in file_list:
    if file_schema.find(".schema") > 0:                 # если очередной файл из кучи файлов *.schema

        with open(file_schema) as f:
            cur_schema = json.load(f)                   #открываем его и сохроняем как текущую схему json 
            
            for file_json in file_list:                  
                if file_json.find(".json") > 0:         #ищем *.json, снова в той куче
                    with open(file_json) as f:          
                        cur_json = json.load(f)         #открываем для дальнейшего прогона на валидность по текущей схеме 

                        instance = cur_json
                        v = Draft3Validator(cur_schema)
                        errors = sorted(v.iter_errors(instance), key=lambda e: e.path)          #сохраняем ошибки валидности, если они есть                        
                        
                        for error in errors:                                                                
                            print(file_json[file_json.rfind("\\"):len(file_json)] , end=" ---> ")       #и если они есть сообщаем для какого *json по какой *schema какого тапа ошибки 
                            print(file_schema[file_schema.rfind("\\"):len(file_schema)], ":")
                            print("Error :",error.message,"\n")
                            

        print("--------------------------------------")
