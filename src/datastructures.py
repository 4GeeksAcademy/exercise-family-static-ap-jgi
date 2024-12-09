
# """
# update this file to implement the following already declared methods:
# - add_member: Should add a member to the self._members list
# - delete_member: Should delete a member from the self._members list
# - update_member: Should update a member from the self._members list
# - get_member: Should return a member from the self._members list
# """
from random import randint
# los metodos son funcioneso acciones  que dependen de la clase
# CLASE QUE CONSTRUYE OBJETOS O MAQUETAS
class FamilyStructure:
    # ESTE SELF (PROPIO) APUNTA A ESTA SOLA CLASE.
    def __init__(self, last_name): # le paso el apellido por parametro 
        self.last_name = last_name
 
       #Almaceno a los miebros de mi familia 
        self._members = []

    #  genero un id aleatoio para cada mimebro de la familia 
    def _generateId(self):
        return randint(0, 99999999)


    # funcion que agrega el miembro a la familia, agregamos el elemnto que recibimos por el parametro members
    # EL SELF SIRVE PARA APUNTAR O DISPONIBILIZAR A JACKSON_FAMILY TODOS LOS METODOS. CADA NUEVO OBJ QUE PARTE DE LA CLASE TIENE SU PROPIO SELF APELLIDO O NOMBRE.
    def add_member(self, member):
        new_member = {
          "id": self._generateId(),
           "first_name" : member["first_name"],
           "age" : member["age"],
           "lucky_numbers" : member["lucky_numbers"]
       }
        self._members.append (new_member)
        return self._members
    


    def delete_member(self, id):
        # fill this method and update the return
          for member in self._members:
            if member["id"] == int(id):
                self._members.remove(member)
                return True 
          return None                                            # return # esta fuera del if y fuera del for 



# MOSTRAR UN SOLO MIEMBRO   
    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == int(id):
                return member  
       # return # esta fuera del if y fuera del for 
        return None 
  # MEOTODO PARA MOSTRAR TODOS LOS MIEMBROS
    def get_all_members(self):
        return self._members
