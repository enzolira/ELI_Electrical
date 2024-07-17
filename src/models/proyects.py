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
    def get_all_tgs_by_user_id(cls,data):
        query = "SELECT	* FROM tgs LEFT JOIN proyects ON proyects.id = tgs.proyect_id WHERE user_id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        tgs = []
        for pro in results:
            tgs.append(pro)
        return tgs


    @classmethod
    def get_all_tgs_by_proyect_id_and_user_id(cls,data):
        query = "SELECT *, proyects.id AS projecto, proyects.name AS projects FROM tgs LEFT JOIN proyects ON proyects.id = tgs.proyect_id WHERE user_id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query,data)
        tds = []
        for pro in results:
            tds.append(pro)
        return tds

    @classmethod
    def get_all_tgs_by_proyect_id(cls,data):
        query = "SELECT * FROM proyects INNER JOIN tgs ON proyects.id = tgs.proyect_id WHERE proyects.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        tgs = []
        for pro in results:
            tgs.append(pro)
        return tgs

    @classmethod
    def delete_proyect_by_proyec_id(cls,data):
        query = "DELETE FROM proyects WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def current(cls, data):
        query = "SELECT singles_break.name AS disyuntor, singles_diff.name AS diferencial, wiresthrv.secction_mm2, wiresthrv." + str(data.get('method')) + " FROM \
            (SELECT * FROM singles_breakers WHERE capacity > " + str(data.get('total_current')) + " * 1.25 OR ABS(capacity - (" + str(data.get('total_current')) + " * 1.25)) < 0.40 ORDER BY capacity LIMIT 1) AS singles_break JOIN \
            (SELECT * FROM singles_elect_diff WHERE capacity > " + str(data.get('total_current')) + " * 1.25 OR ABS(capacity - (" + str(data.get('total_current')) + " * 1.25)) < 0.40 ORDER BY capacity LIMIT 1) AS singles_diff JOIN \
            (SELECT * FROM wiresthrv WHERE " + str(data.get('method')) + " > " + str(data.get('total_current')) + " * 1.25 OR ABS( " + str(data.get('method')) + " - (" + str(data.get('total_current')) + " * 1.25)) < 0.40 ORDER BY secction_mm2 LIMIT 1) AS wiresthrv ON 1=1;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result


    @classmethod
    def current_tri(cls, data):
        query = "SELECT disyuntor, diferencial, wiresthrv.secction_mm2, wiresthrv." + str(data.get('method')) + " FROM \
            (SELECT * FROM three_breakers WHERE capacity > " + str(data.get('total_current')) + " * 1.25 OR ABS(capacity - (" + str(data.get('total_current')) + " * 1.25)) < 0.40 ORDER BY capacity LIMIT 1) AS three_breaker JOIN \
            (SELECT * FROM three_elect_diff WHERE capacity > " + str(data.get('total_current')) + " * 1.25 OR ABS(capacity - (" + str(data.get('total_current')) + " * 1.25)) < 0.40 ORDER BY capacity LIMIT 1) AS three_elect_dif JOIN \
            (SELECT * FROM wiresthrv WHERE " + str(data.get('method')) + " > " + str(data.get('total_current')) + " * 1.25 OR ABS( " + str(data.get('method')) + " - (" + str(data.get('total_current')) + " * 1.25)) < 0.40 ORDER BY secction_mm2 LIMIT 1) AS wiresthrv ON 1=1;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result



    @classmethod
    def get_all_wires(cls):
        query = "SELECT * FROM wires"
        results = connectToMySQL(cls.db).query_db(query)
        return results


    @classmethod
    def get_all_details_by_proyects(cls, data):
        query = "SELECT \
                (SELECT COUNT(tgs.id) FROM tgs LEFT JOIN proyects ON proyects.id = tgs.proyect_id WHERE proyects.id = %(proyect_id)s) AS TG, \
                (SELECT COUNT(tds.id) FROM tds LEFT JOIN tgs ON tgs.id = tds.tg_id JOIN proyects ON proyects.id = tgs.proyect_id WHERE proyects.id = %(proyect_id)s) AS TD, \
                (SELECT COUNT(circuits.id) FROM circuits LEFT JOIN tgs ON tgs.id = circuits.tg_id LEFT JOIN proyects ON proyects.id = tgs.proyect_id WHERE proyects.id = %(proyect_id)s) AS CTSTG, \
                (SELECT COUNT(circuits.id) FROM circuits LEFT JOIN tds ON tds.id = circuits.td_id LEFT JOIN tgs ON tgs.id = tds.tg_id LEFT JOIN proyects ON proyects.id = tgs.proyect_id WHERE proyects.id = %(proyect_id)s) AS CTSTD \
                FROM dual;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
