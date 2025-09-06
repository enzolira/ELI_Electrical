from flask import flash
from src.config.mysqlconnection import connectToMySQL

class Floor:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.piso = data['piso']
        self.trasc = data['trasc']
        self.shopping_id = data['shopping_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_floor(cls,data):
        query = "INSERT INTO floor (piso, trasc, shopping_id, created_at, updated_at) VALUES (%(floor)s, %(trasc)s, %(shopping_id)s, NOW(), NOW());"
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        return result
    
    @classmethod
    def get_all_floor(cls,data):
        query = "SELECT * FROM floor WHERE shopping_id = %(shopping_id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        return result
    
    @classmethod
    def get_floor_by_id(cls, data):
        query = "SELECT * FROM floor WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if result:
            return cls(result[0])  # Devuelve objeto Floor
        return None
    