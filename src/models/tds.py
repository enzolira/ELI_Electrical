from flask import Flask
from src.config.mysqlconnection import connectToMySQL

class Tds:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.tg_id = data['tg_id']
        self.name = data['name']
        self.tag = data['tag']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_tds(cls, data):
        query = "INSERT INTO tds (tg_id, name, tag, created_at, updated_at) VALUES (%(tg_id)s, %(name)s, %(tag)s, NOW(), NOW())"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    

    @classmethod
    def get_all_tds_by_tg_id(cls, data):
        query = "SELECT * FROM tds WHERE tg_id = " + str(data.get('tg_id')) + ";"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        if (not results):
            return []
        tds = []
        for i in results:
            tds.append(i)
            print(tds)
        return tds
