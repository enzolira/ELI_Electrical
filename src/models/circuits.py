from flask import flash
from src.config.mysqlconnection import connectToMySQL

class Circuit:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.ref = data['ref']
        self.total_center = data['total_center']
        self.single_voltage = data['simgle_voltage']
        self.fp = data['fp']
        self.method = data['method']
        self.sumary_current = data['sumary_current']
        self.type_circuit = data['type_circuit']
        self.type_vp = data['vp']
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
        query = "INSERT INTO circuits (name, ref, total_center, single_voltage, fp, method, sumary_current, type_circuit, vp, length, secctionmm2, wires, current_by_method, created_at, updated_at, tg_id, td_id) VALUES (%(name)s, %(ref)s, NULL, %(single_voltage)s, %(fp)s, %(method)s, NULL, %(type_circuit)s, NULL, %(length)s, NULL, %(wires)s, NULL, NOW(), NOW(), %(tg_id)s, NULL);"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def update_circuits(cls, data):
        query = "UPDATE circuits SET secctionmm2 = %(secctionmm2)s, current_by_method = %(current_by_method)s, vp = %(vp_real)s, sumary_current = (SELECT SUM(total_current) FROM loads) WHERE circuits.id = %(circuit_id)s, "
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    # @staticmethod
    # def validate_circuit(data):
    #     is_valid = True
    #     if not data['name']:
    #         flash("Ingresa el numero de circuito !!!","circuito")
    #         is_valid = False
    #     if not data['voltage']:
    #         flash("Ingresa el voltage del circuito !!!","circuito")
    #         is_valid = False
    #     if not data['methods']:
    #         flash("Ingresa el tipo de metodo del circuito !!!","circuito")
    #         is_valid = False
    #     if not data['qty']:
    #         flash("Ingresa la cantidad de cargas del circuito !!!","circuito")
    #         is_valid = False
    #     if not data['load']:
    #         flash("Ingresa la potencia de cada carga del circuito !!!","circuito")
    #         is_valid = False
    #     if not data['length']:
    #         flash("Ingresa el largo del circuito !!!","circuito")
    #         is_valid = False
    #     return is_valid
