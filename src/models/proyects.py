from flask import flash
from src.config.mysqlconnection import connectToMySQL

class Proyect:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO proyects (name, user_id, created_at, updated_at) VALUES(%(name)s,%(user_id)s, NOW(),NOW())"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_all_proyect_by_user_id(cls,data):
        query = "SELECT	* FROM proyects LEFT JOIN users ON user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        proyects = []
        for pro in results:
            proyects.append(pro)
        return proyects

    @classmethod
    def get_all_tgs_by_proyect_id_and_user_id(cls,data):
        query = "SELECT tgs.name FROM tgs LEFT JOIN proyects ON proyects.id = tgs.proyect_id WHERE user_id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query,data)
        tds = []
        for pro in results:
            tds.append(pro)
        return tds
    
    
    @classmethod
    def current(cls,data):
        query = "SELECT * FROM wiresthrv WHERE " + data.get('method') + " >= %(total_current)s OR ABS(" + data.get('method') + " - %(total_current)s ) < 0.20 ORDER BY " + data.get('method') + " LIMIT 1;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result
    
    @classmethod
    def get_all_wires(cls):
        query = "SELECT * FROM wires"
        results = connectToMySQL(cls.db).query_db(query)
        return results

    

    @staticmethod
    def validate_circuit(data):
        is_valid = True
        if not data['name']:
            flash("Ingresa el numero de circuito !!!","circuito")
            is_valid = False
        if not data['single_voltage']:
            flash("Ingresa el voltage del circuito !!!","circuito")
            is_valid = False
        if not data['method']:
            flash("Ingresa el tipo de metodo del circuito !!!","circuito")
            is_valid = False
        if not data['qty']:
            flash("Ingresa la cantidad de cargas del circuito !!!","circuito")
            is_valid = False
        if not data['power']:
            flash("Ingresa la potencia de cada carga del circuito !!!","circuito")
            is_valid = False
        if not data['length']:
            flash("Ingresa el largo del circuito !!!","circuito")
            is_valid = False
        return is_valid
