from flask import flash
from src.config.mysqlconnection import connectToMySQL

class Report:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.centro = data['centro']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['update_at']

    @classmethod
    def save_shopping(cls,data):
        query = "INSERT INTO shopping (centro, user_id, created_at, updated_at) VALUES (%(centro)s, %(user_id)s, NOW(), NOW());"
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        return result
    
    @classmethod
    def get_all_shopping_by_user_id(cls,data):
        query = "SELECT * FROM shopping WHERE user_id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query,data)
        mall = []
        for job in result:
            mall.append(job)
        return mall
    
    @classmethod
    def get_all_floor_by_shopping(cls,data):
        query = "SELECT * FROM floor INNER JOIN shopping ON flo.proyect_id = proyects.id WHERE proyects.id = %(proyect_id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        job = []
        for xl in result:
            job.append(xl)
        return job
    
    @classmethod
    def get_shopping_by_id(cls, data):
        query = "SELECT * FROM shopping WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            return result[0]  # Devuelve solo el primer resultado como diccionario
        return None
    