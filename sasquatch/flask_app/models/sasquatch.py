from flask import Flask, render_template, redirect, session, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import login
from flask import flash

# Look at the bottom and fix it

class Sasquatch:
    db = "sasquatch"
    def __init__( self , data ):
        self.id = data['id']
        self.location = data['location']
        self.date = data['date']
        self.number = data['number']
        self.happened = data['happened']
        self.host_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.host = None



    #Create recipe Models

    @classmethod
    def create_sasquatch(cls, data):
        if not cls.validate_sasquatch_data(data): return False
        query = """
            INSERT INTO quatch
                (location, date, number, happened, user_id)
            VALUES
                (%(location)s, %(date)s, %(number)s, %(happened)s, %(user_id)s)
            ;"""
        return connectToMySQL(cls.db).query_db(query, data)

    #read recipe Models

    @classmethod
    def get_all_sasquatch_w_hosts(cls):
        query = """
            SELECT * 
            FROM quatch
            JOIN users
            ON  users.id = quatch.user_id
            ;"""
        results = connectToMySQL(cls.db).query_db(query)
        quatch = []
        for result in results:
            this_sasquatch = cls(result)
            this_sasquatch.host = login.Login.instantiate_user(result)
            quatch.append(this_sasquatch)
        return quatch

    @classmethod
    def get_sasquatch_by_id_w_host(cls, id):
        data = {'id' : id}
        query = """
            SELECT * 
            FROM quatch
            JOIN users
            ON  users.id = quatch.user_id
            WHERE quatch.id = %(id)s
            ;"""
        result = connectToMySQL(cls.db).query_db(query, data)
        this_sasquatch = cls(result[0])
        this_sasquatch.host = login.Login.instantiate_user(result[0])
        return this_sasquatch


    #update recipe Models   

    @classmethod
    def update_sasquatch(cls, data):
        if not cls.validate_sasquatch_data(data): return False
        query = """
            UPDATE quatch
            SET 
                location = %(location)s,
                date = %(date)s,
                number = %(number)s,
                happened = %(happened)s
            WHERE id = %(id)s
            ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return True


    #delete recipe Models

    @classmethod
    def delete_sasquatch_by_id(cls,id):
        data = {'id' : id}
        query = """
            DELETE FROM quatch
            WHERE id = %(id)s
            ;"""
        connectToMySQL(cls.db).query_db(query, data)
        return 



    #Validations

    @classmethod
    def validate_sasquatch_data(cls,data):
        is_valid = True 
        if len(data['location']) == 0 :
            flash("Location is required.")
            is_valid = False
        if not data['date']:
            flash('A date is required')
            is_valid = False
        if len(data['number']) < 1:
            flash('numbers field should be at least 1 minutes')
            is_valid = False
        if len(data['happened']) < 50:
            flash('Notes on what happened should be at least 50 characters')
            is_valid = False 
        return is_valid
