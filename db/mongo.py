import pymongo as pm

def connect():
    #establecer la cvonexion con el servidor
    cliente =pm.MongoClient("mongodb://localhost:27017/")

    #Seleccionar una base de datos y la colección
    bd = cliente ["GestorInventarioDB"]
    coleccion = bd ["Usuarios"]

    print("conectado")

    #Realizar una consulta a la colección 
    resultados = coleccion.find()

    users = []
    for resultado in resultados:
        users.append(resultado["nombre"])

#Imprimir el resultado
    print(users)
    #return users