from flask import Flask
from src.config.mysqlconnection import connectToMySQL

class Tgs:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.tag = data['tag']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.proyect_id = data['proyect_id']


    @classmethod
    def add_tgs(cls,data):
        query = "INSERT INTO tgs (name, tag,created_at, updated_at, proyect_id) VALUES (%(name)s, %(tag)s, NOW(), NOW(), %(proyect_id)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_tgs_by_project(cls,data):
        query = "SELECT * FROM tgs WHERE proyect_id = %(proyect_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if (not result):
            return []
        tgs = []
        for elmt in result:
            tgs.append(elmt)
        return tgs
