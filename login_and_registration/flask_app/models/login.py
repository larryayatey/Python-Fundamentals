from flask import Flask, render_template, redirect, session, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)
import re


class Login:
    db = "login_and_registration"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM login;"
        results = connectToMySQL('login_and_registration').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users
            

    @classmethod
    def save(cls, data):
        if not cls.validate_login(data):return False
        data = data.copy()
        data['password'] = bcrypt.generate_password_hash(data['password'])
        query = """
            INSERT INTO login (first_name, last_name, email, password)
            VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        """
        user_id = connectToMySQL(cls.db).query_db(query, data)
        session ['user_id'] = user_id
        session ['user_name'] = f'{data['first_name']}{data['last_name']}'
        return user_id

    @classmethod
    def get_by_email(cls, email):
        data = {'email': email}
        query = """
            SELECT * FROM login
            WHERE email = %(email)s;
        """
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def login(cls, data):
        this_user = cls.get_by_email(data['email'])
        if this_user:
            if bcrypt.check_password_hash(this_user.password, data['password']):
                session['user_id'] = this_user.id
                session['user_name'] = f'{this_user.first_name} {this_user.last_name}'
                return True
        flash('Invalid Email/Password')
        return False

    @classmethod
    def validate_login(cls,data):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(data.get("first_name")) < 3:
            flash("First name must be at least 3 characters")
            is_valid = False

        if len(data.get("last_name")) < 3:
            flash("Last name must be at least 3 characters")
            is_valid = False

        if len(data.get('password')) < 8:
            flash('Password must be atleast 8 characters long and should be a mix between letters and numbers.')
            is_valid = False

        if data.get("password") != data.get("confirm_password"):
            flash("Password must match")
            is_valid = False

        if not EMAIL_REGEX.match(data.get("email")):
            flash("Invalid email/Password ")
            is_valid = False 

        if cls.get_by_email(data['email']):
            is_valid = False
            flash('Email Already Exists, Please login')
        return is_valid
