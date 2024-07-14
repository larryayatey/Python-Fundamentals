from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db = "users_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
            

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        return connectToMySQL("users_schema").query_db(query, data)
        

    @classmethod
    def delete(cls, id):
        data = {"id":id}
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    

    @classmethod
    def read(cls, id):
        data = {"id":id}
        query = """ SELECT * FROM users
                    WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    

    @classmethod
    def edit(cls, data):
        query= """
                UPDATE users SET 
                first_name = %(first_name)s,
                last_name = %(last_name)s,
                email = %(email)s,
                updated_at = NOW()
                WHERE id = %(id)s;
            """
        return connectToMySQL(cls.db).query_db(query, data)
