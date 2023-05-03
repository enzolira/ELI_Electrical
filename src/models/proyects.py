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
    def get_all_tds_by_proyect_id_and_user_id(cls,data):
        query = "SELECT	* FROM tds LEFT JOIN proyects ON proyects.id = tds.proyect_id \
            LEFT JOIN users ON users.id = proyects.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        tds = []
        for pro in results:
            tds.append(pro)
        return tds
    
    @classmethod
    def seccion(cls,data):
        query = "SELECT * FROM wiresthrv WHERE secction_mm2 > %(secc_min)s OR ABS(secction_mm2 - %(secc_min)s) < 0.40 ORDER BY secction_mm2 LIMIT 1;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result
    
    @classmethod
    def current(cls,data):
        query = "SELECT * FROM wiresthrv WHERE %(method)s >= %(total_current)s OR ABS(%(method)s - %(total_current)s ) < 0.20 ORDER BY %(method)s LIMIT 1;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result


    # @classmethod
    # def methods_wiresthrv(cls,data):
    #     query = "SELECT * FROM wiresthrv WHERE %(method)s = %(scalmin)s;"
    #     result = connectToMySQL(cls.db).query_db(query,data)
    #     return result

    # @classmethod
    # def methodds_wiresh07z(cls,scalmin,methods):
    #     query = "SELECT * FROM wiresh07z WHERE %(methods)s = %(scalmin)s;"
    #     result = connectToMySQL(cls.db).query_db(query,scalmin,methods)
    #     return result
    

    @staticmethod
    def validate_circuit(data):
        is_valid = True
        if not data['name']:
            flash("Ingresa el numero de circuito !!!","circuito")
            is_valid = False
        if not data['voltage']:
            flash("Ingresa el voltage del circuito !!!","circuito")
            is_valid = False
        if not data['methods']:
            flash("Ingresa el tipo de metodo del circuito !!!","circuito")
            is_valid = False
        if not data['qty']:
            flash("Ingresa la cantidad de cargas del circuito !!!","circuito")
            is_valid = False
        if not data['lenght']:
            flash("Ingresa el largo del circuito !!!","circuito")
            is_valid = False
        return is_valid
