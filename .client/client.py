import json, os, random

def writeReadme(_id, role):
    with open('../README.md', 'a+') as file:
        file.write(f'bot\t{_id} role\t{role}\n')

def idRand():
    _id = random.randint(999, 99999)
    return _id

def createConfig():
    _id, role = idRand(), "0"
    with open('../README.md', 'r') as file:
        idcontrol = file.read()
        if str(_id) not in idcontrol:pass
        else:createConfig()
    
    newObj = {
            "id":_id,
            "role":role
            }
    with open('config.json', 'w') as file:
        json.dump(newObj, file)
    writeReadme(_id, role)

def searchJson():
    state = False
    CONFIG = 'config.json'
    for file in os.listdir():
        if CONFIG in file:stateConfig = True
        else:stateConfig = False

    return stateConfig
            

def client():
    if searchJson():
        print('Конфиг есть')
    else:
        print('Конфига нет')
        createConfig()

client()
