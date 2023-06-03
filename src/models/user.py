from flask import flash
from src.config.mysqlconnection import connectToMySQL

import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.company = data['company']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,company,email,password,created_at, updated_at) VALUES(%(first_name)s,%(last_name)s,%(company)s,%(email)s,%(password)s,NOW(),NOW())"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_new_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query,user)
        if len(results) >= 1:
            flash("Email ya registrado","new_register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Email invalido!!!","new_register")
            is_valid=False
        if len(user['first_name']) < 2:
            flash("FNombre debe contener 2 caracteres minimo","new_register")
            is_valid= False
        if len(user['last_name']) < 3:
            flash("Apellido debe contener 3 caracteres minimo","new_register")
            is_valid= False
        if len(user['company']) < 5:
            flash("Empresa debe contener 5 caracteres minimo","new_register")
        if len(user['password']) < 6:
            flash("Password must be at least 6 characters","new_register")
            is_valid= False
        if user['password'] != user['confpw']:
            flash("Passwords don't match","new_register")
        return is_valid