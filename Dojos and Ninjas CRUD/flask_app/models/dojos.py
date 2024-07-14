from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas import Ninja
from pprint import pprint 

class Dojo:
    db = "dojoandninjacrud"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojoandninjacrud').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
            

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL("dojoandninjacrud").query_db(query, data)
        

    @classmethod 
    def get_dojo_ninjas(cls, dojo_id):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s;"
        data = {
            "dojo_id": dojo_id
        }
        list_dicts = connectToMySQL("dojoandninjacrud").query_db(query, data)
        dojo = Dojo(list_dicts[0])
        for each_dict in list_dicts:
            ninjas_data = {
                "id": each_dict['ninjas.id'],
                "first_name": each_dict['first_name'],
                "last_name": each_dict['last_name'],
                "age": each_dict['age'],
                "dojo_id": each_dict['dojo_id'],
                "created_at": each_dict['ninjas.created_at'],
                "updated_at": each_dict['ninjas.updated_at'],
            }
            dojo.ninjas.append(Ninja(ninjas_data))
        return dojo