"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
# IMPORTACIONES 
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
# desde el archivo datastructures trae la info
from datastructures import FamilyStructure
#from models import Person

#config de la aplicacion
app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# crear una instancia de la clase familyStructures !!!!!!!!!
# // en una variable creamos un objeto y tiene la estructura de familystructures
# jackson es el parametro de last_name de nuestro data.structures, este obj tiene disponible agregar, eliminar, objener y listar miembros
# # ademas tiene la propiedad last name y members, ejm PRINT (JACKSON_FAMILY.LAST_NAME) (ACCEDO AL APELLIDO) 

jackson_family = FamilyStructure("Jackson") #  es un objeto creado a partir de la clase FamilyStructure. Este objeto representa la familia "Jackson".
#PODEMOS AGREGAR UNA NUEVA FAMILIA
# perez_family =  FamilyStructure("perez")
# Agregamos miembros a la familia Jackson
jackson_family._members.append(
    {
        "id": jackson_family._generateId(),
        "first_name": "John Jackson",
        "age": 33,
        "lucky_numbers": [7, 13, 22]
    }
)

jackson_family._members.append(
    {
        "id": jackson_family._generateId(),
        "first_name": "Jane Jackson",
        "age": 35,
        "lucky_numbers": [10, 14, 3]
    }
)

jackson_family._members.append(
    {
        "id": jackson_family._generateId(),
        "first_name": "Jimmy Jackson",
        "age": 5,
        "lucky_numbers": [1]
    }
)


 #GESTIONA ERRORES DE LA WEB 
# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# // CREA LA PAGINA QUE VEMOS EN LA WEB 
@app.route('/')
def sitemap():
    return generate_sitemap(app)


#este get sirve para obtener todos los miembros
@app.route('/members', methods=['GET'])
def all_members():

# entrega un listado de los miembros y los almacena en members
    members = jackson_family.get_all_members() # seria acceder a los objetos de datastructures con jackson y con get_all_members, accedemos a sus miembros
    return jsonify(members), 200


# este get sirve para obtener un solo miembro 
@app.route('/member/<int:id>', methods=['GET'])
def one_member(id):
    member = jackson_family.get_member(id)
    if member == None: 
        return "Usuario no encontrado", 400
    member_dto = {
        "name" : member["first_name"],
        "id" : member["id"],
        "age" : member["age"],
        "lucky_numbers" : member["lucky_numbers"]
    }
    return jsonify(member_dto), 200


#ELIMINAR MIEMBRO
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_one_member(id):
    member = jackson_family.delete_member(id)
    if member == None: 
        return "User not exist", 400
    body = {
       "done": True
    }
    return jsonify(body), 200



# probamos enviando infor con postman 
# En este codigo recibimos el new member por la api y al objeto jackson family le agregamos el data_new_member que contiene el nuevo miembro (funcion independiente que contiene el new member) 
# jackson_family.add_member = accedemos al metodo de data structures llamado add_member que se encarga de agregar a la lista e nuevo miembro.
@app.route('/member', methods=['POST'])
def add_member():
   data_new_member = request.json() #recibimos la info del nuevo miembro  en formato json o formate diccionario
   if not data_new_member:
       return "Faltan datos en tu solicitud", 400 # solucionar (mostrar error)
   member_update =  jackson_family.add_member(data_new_member) 
   return jsonify(member_update), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
