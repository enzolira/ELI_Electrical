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
        query = "SELECT * FROM tgs LEFT JOIN proyects ON proyects.id = tgs.proyect_id WHERE user_id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query,data)
        tds = []
        for pro in results:
            tds.append(pro)
        return tds
    

    
    @classmethod
    def current(cls, data):
        query = "SELECT singles_break.name AS disyuntor, singles_diff.name AS diferencial, wiresthrv.secction_mm2, wiresthrv." + str(data.get('method')) + " FROM \
            (SELECT * FROM singles_breakers WHERE capacity > " + str(data.get('total_current')) + " OR ABS(capacity - " + str(data.get('total_current')) + ") < 0.40 ORDER BY capacity LIMIT 1) AS singles_break JOIN \
            (SELECT * FROM singles_elect_diff WHERE capacity > " + str(data.get('total_current')) + " OR ABS(capacity - " + str(data.get('total_current')) + ") < 0.40 ORDER BY capacity LIMIT 1) AS singles_diff JOIN \
            (SELECT * FROM wiresthrv WHERE " + str(data.get('method')) + " > " + str(data.get('total_current')) + " OR ABS( " + str(data.get('method')) + " - " + str(data.get('total_current')) + ") < 0.40 ORDER BY secction_mm2 LIMIT 1) AS wiresthrv ON 1=1;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def updated_current(cls, data):
        query = "SELECT singles_break.name AS disyuntor, singles_diff.name AS diferencial, wiresthrv.secction_mm2, wiresthrv." + str(data.get('method')) + " FROM \
            (SELECT * FROM singles_breakers WHERE capacity > " + str(data.get('total_current')) + " OR ABS(capacity - " + str(data.get('total_current')) + ") < 0.40 ORDER BY capacity LIMIT 1) AS singles_break JOIN \
            (SELECT * FROM singles_elect_diff WHERE capacity > " + str(data.get('total_current')) + " OR ABS(capacity - " + str(data.get('total_current')) + ") < 0.40 ORDER BY capacity LIMIT 1) AS singles_diff JOIN \
            (SELECT * FROM wiresthrv WHERE " + str(data.get('method')) + " > " + str(data.get('total_current')) + " OR ABS( " + str(data.get('method')) + " - " + str(data.get('total_current')) + ") < 0.40 ORDER BY secction_mm2 LIMIT 1) AS wiresthrv ON 1=1;"
        result = connectToMySQL(cls.db).query_db(query, data)
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
