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
        self.breakers = data['breakers']
        self.total_center = data['total_center']
        self.total_current_ct = data['total_current_ct']
        self.total_power_ct = data['total_power_ct']
        self.elec_differencial = data['elect_differencial']
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
    def get_all_circuits_by_tg_id(cls, data):
        query = "SELECT * FROM loads LEFT JOIN circuits ON circuits.id = loads.circuit_id WHERE circuits.tg_id = %(tg_id)s AND circuits.td_id IS NULL;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if (not results):
            return []
        circuit_tg_id = []
        for ct_tg in results:
            circuit_tg_id.append(ct_tg)
        return circuit_tg_id
    
    @classmethod
    def get_all_circuit_and_tds_by_tg(cls, data):
        query = "SELECT *, circuits.id FROM loads LEFT JOIN circuits ON circuits.id = loads.circuit_id WHERE circuits.tg_id = %(tg_id)s AND circuits.td_id = %(td_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        if (not results):
            return []
        circuit_tds = []
        for ctd in results:
            circuit_tds.append(ctd)
        return circuit_tds

    @classmethod
    def detail_circuit_and_loads_by_id(cls, data):
        query = "SELECT *, loads.id AS burden , circuits.length AS largo FROM loads LEFT JOIN circuits ON circuits.id = loads.circuit_id WHERE circuits.id = %(circuit_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        circuits = []
        if (not results):
            return []
        for ct in results:
            circuits.append(ct)
        return circuits

    @classmethod
    def detail_circuit_by_id(cls, data):
        query = "SELECT * FROM circuits WHERE id = %(circuit_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        circuits = []
        if (not results):
            return []
        for ct in results:
            circuits.append(ct)
        return circuits


    @classmethod
    def add_circuit(cls,data):
        query = "INSERT INTO circuits (name, ref, single_voltage, fp, method, type_circuit, vp, length, secctionmm2, wires, current_by_method, breakers, elect_differencial, total_center, total_current_ct, total_power_ct, created_at, updated_at, tg_id, td_id) VALUES \
                (%(name)s, %(ref)s, %(single_voltage)s, %(fp)s, %(method)s, %(type_circuit)s, NULL, %(length)s, NULL, %(wires)s, NULL, NULL, NULL, NULL, NULL, NULL, NOW(), NOW(), %(tg_id)s, %(td_id)s);"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    @classmethod
    def update_method(cls, data):
        query = "UPDATE circuits SET current_by_method = %(current_by_method)s WHERE circuits.id = %(circuit_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def vp_real(cls, data):
        query = "SELECT secction_mm2 , " + str(data.get('method')) + " AS method  FROM wiresthrv WHERE " + str(data.get('method')) + " > " + str(data.get('total_current')) + ";"
        results = connectToMySQL(cls.db).query_db(query, data)
        currents = []
        if (not results):
            return []
        for cu in results:
            currents.append(cu)
        return currents
    
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

    @classmethod
    def update_breakers(cls, data):
        query = "UPDATE circuits SET breakers = %(breakers)s WHERE circuits.id = %(circuit_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def update_elect_differencial(cls, data):
        query = "UPDATE circuits SET elect_differencial = %(elect_differencial)s WHERE circuits.id = %(circuit_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def updated_loads(cls, data):
        query = "UPDATE circuits SET total_center = (SELECT SUM(qty) FROM loads WHERE circuit_id = %(circuit_id)s), total_current_ct = (SELECT SUM(total_current) FROM loads WHERE circuit_id = %(circuit_id)s), total_power_ct = (SELECT SUM(total_power) FROM loads WHERE circuit_id = %(circuit_id)s) WHERE circuits.id = %(circuit_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result    