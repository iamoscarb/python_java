import requests

#pasa los datos del archivo txt a una lista bidimencional
def read_data():
    dts=[]
    with open("files/Clientes.txt") as data:
        for lines in data:
            character=lines.replace("\n","") #borra el \n del salto de linea
            dts.append(character.split(", ")) #los datos estan separados por una coma y un espacio

    return dts

#manda los datos de un diccionario al local host
def send_data(data):
    #se inicializa un diccionario
    todo={}
    #url con la direccion con la que trabajamos
    api_url="http://localhost:8080/apiv1/clients/add"

    #con un for va cargando los datos al diccionario, al reiniciarse el ciclo, cambian los valores
    for i in range(len(data)):
        todo['firstname'] = data[i][0]
        todo['surname'] = data[i][1]
        todo['country'] = data[i][2]
        todo['language'] = data[i][3]
        todo['airport'] = data[i][4]

        #mandamos el diccionario de datos a la url
        response = requests.post(api_url, json=todo)
        response.json()
    
    airport("")
    country("")
    language("")


def show_data_clients():
    api_url="http://localhost:8080/apiv1/clients/listClients"
    response=requests.get(api_url)
    data = response.json()
    return data

def new_data():
    name=input("Name: ")
    surname=input("Surname: ")
    country=input("Country: ")
    language=input("Language: ")
    airport=input("airport: ")

    dts=[name,surname,country,language,airport]

    todo={}
    api_url="http://localhost:8080/apiv1/clients/add"
  
    todo['firstname'] = dts[0]
    todo['surname'] = dts[1]
    todo['country'] = dts[2]
    todo['language'] = dts[3]
    todo['airport'] = dts[4]
    #mandamos el diccionario de datos a la url
    response = requests.post(api_url, json=todo)
    response.json()
    
    airport(dts[4])
    country(dts[2])
    language(dts[3])



def airport(airl):
    data="http://localhost:8080/airport/add"
    todo={}
    dta = show_data_clients()
    print(dta)
    for i in range(len(dta)):
        print(dta[i]['airport'])
        if dta[i]['airport'] != str(airl):
            todo['arName'] = dta[i]['airport']
            response = requests.post(data, json=todo)
            response.json()


def country(country):
    data="http://localhost:8080/country/add"
    todo={}
    dta = show_data_clients()
    print(dta)
    for i in range(len(dta)):
        print(dta[i]['country'])
        if dta[i]['country'] != str(country):
            todo['cName'] = dta[i]['country']
            response = requests.post(data, json=todo)
            response.json()

def language(language):
    data="http://localhost:8080/languages/add"
    todo={}
    dta = show_data_clients()
    print(dta)
    for i in range(len(dta)):
        print(dta[i]['language'])
        if dta[i]['language'] != str(language):
            todo['langName'] = dta[i]['language']
            response = requests.post(data, json=todo)
            response.json()

