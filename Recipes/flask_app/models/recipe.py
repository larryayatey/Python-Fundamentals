from flask import Flask, render_template, redirect, session, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import login
from flask import flash

# Look at the bottom and fix it

class Recipe:
    db = "recipes"
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date = data['date']
        self.host_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.host = None



    #Create recipe Models

    @classmethod
    def create_recipe(cls, data):
        if not cls.validate_recipe_data(data): return False
        query = """
            INSERT INTO newrecipe 
                (name, description, instructions, under_30, date, user_id)
            VALUES
                (%(name)s, %(description)s, %(instructions)s, %(under_30)s, %(date)s, %(user_id)s)
            ;"""
        return connectToMySQL(cls.db).query_db(query, data)

    #read recipe Models

    @classmethod
    def get_all_recipes_w_hosts(cls):
        query = """
            SELECT * 
            FROM newrecipe
            JOIN users
            ON  users.id = newrecipe.user_id
            ;"""
        results = connectToMySQL(cls.db).query_db(query)
        newrecipe = []
        for result in results:
            this_recipe = cls(result)
            this_recipe.host = login.Login.instantiate_user(result)
            newrecipe.append(this_recipe)
        return newrecipe

    @classmethod
    def get_recipe_by_id_w_host(cls, id):
        data = {'id' : id}
        query = """
            SELECT * 
            FROM newrecipe
            JOIN users
            ON  users.id = newrecipe.user_id
            WHERE newrecipe.id = %(id)s
            ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        this_recipe = cls(result[0])
        this_recipe.host = login.Login.instantiate_user(result[0])
        return this_recipe


    #update recipe Models   

    @classmethod
    def update_recipe(cls, data):
        if not cls.validate_recipe_data(data): return False
        query = """
            UPDATE newrecipe
            SET 
                name = %(name)s,
                description = %(description)s,
                instructions = %(instructions)s,
                under_30 = %(under_30)s,
                date = %(date)s
            WHERE id = %(id)s
            ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return True


    #delete recipe Models

    @classmethod
    def delete_recipe_by_id(cls,id):
        data = {'id' : id}
        query = """
            DELETE FROM newrecipe
            WHERE id = %(id)s
            ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return 



    #Validations

    @classmethod
    def validate_recipe_data(cls,data):
        print("data",data)
        is_valid = True 
        if len(data['name']) < 3:
            flash('Name field is required and must be at least 3 characters')
            is_valid = False
        if len(data['description']) < 3:
            flash('Description field is required and must be at least 3 characters')
            is_valid = False
        if len(data['instructions']) < 3:
            flash('Instructions field is required and must be at least 3 characters')
            is_valid = False
        if not data['date']:
            flash('A date is required')
            is_valid = False
        if not data.get('under_30'):
            flash('Does your recipe take less than 30 min?')
            is_valid = False 
        #Fix this tmmr
        return is_valid