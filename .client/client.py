import json, os, random

def idRand():
    _id = random.randint(999, 99999)
    return _id

def createConfig():
    _id = idRand()
    print(_id)
    with open('../README.md', 'r') as file:
        idcontrol = file.read()
        if str(_id) not in idcontrol:print('ID уникален')
        else:
            print('ID уже есть')
            createConfig()

        

def searchJson():
    state = False
    CONFIG = ' config.json'
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
