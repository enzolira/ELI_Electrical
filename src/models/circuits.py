from flask import flash
from src.config.mysqlconnection import connectToMySQL

class Circuit:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.ref = data['ref']
        self.single_voltage = data['single_voltage']
        self.fp = data['fp']
        self.method = data['method']
        self.type_circuit = data['type_circuit']
        self.vp = data['vp']
        self.length = data['length']
        self.seccionmm2 = data['secctionmm2']
        self.wires = data['wires']
        self.current_by_method = data['current_by_method']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.tg_id = data['tg_id']
        self.td_id = data['td_id']

    
    @classmethod
    def get_all_circuits_by_user_user_id(cls, data):
        query = "SELECT * FROM loads LEFT JOIN circuits ON circuits.id = loads.circuit_id LEFT JOIN tgs ON tgs.id = circuits.tg_id \
                LEFT JOIN proyects ON proyects.id = tgs.proyect_id LEFT JOIN users ON users.id = proyects.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if (not results):
            return []
        circuits = []
        for ct in results:
            circuits.append(ct)
        return circuits


    @classmethod
    def add_circuit(cls,data):
        query = "INSERT INTO circuits (name, ref, single_voltage, fp, method, type_circuit, vp, length, secctionmm2, wires, current_by_method, created_at, updated_at, tg_id, td_id) VALUES (%(name)s, %(ref)s, %(single_voltage)s, %(fp)s, %(method)s, %(type_circuit)s, NULL, %(length)s, NULL, %(wires)s, NULL, NOW(), NOW(), %(tg_id)s, NULL);"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def update_method(cls, data):
        query = "UPDATE circuits SET current_by_method = %(current_by_method)s WHERE circuits.id = %(circuit_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def update_vp(cls, data):
        query = "UPDATE circuits SET vp = %(vp)s WHERE circuits.id = %(circuit_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def update_secctionmm2(cls, data):
        query = "UPDATE circuits SET secctionmm2 = %(secctionmm2)s WHERE circuits.id = %(circuit_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
