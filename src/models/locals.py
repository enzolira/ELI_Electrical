from flask import flash
from src.config.mysqlconnection import connectToMySQL

class Local:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.numero = data['numero']
        self.marca = data['marca']
        self.floor_id = data['floor_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_local(cls,data):
        query = "INSERT INTO local (numero, marca, floor_id, created_at, updated_at) VALUES (%(numero)s, %(marca)s, %(floor_id)s, NOW(), NOW());"
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        return result
    
    @classmethod
    def get_all_local(cls,data):
        query = "SELECT * FROM local WHERE floor_id = %(floor_id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        return result
    
    @staticmethod
    def validate_local(local: dict) -> bool:
        return bool(local.get("marca")) and isinstance(local.get("numero"), int) and isinstance(local.get("floor_id"), int)
    
    @classmethod
    def get_local_by_id(cls, data):
        query = "SELECT * FROM local WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            return cls(result[0])  # Devuelve objeto Local
        return None

    