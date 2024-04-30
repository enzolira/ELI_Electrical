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
        self.conduit = data['conduit']
        self.wires = data['wires']
        self.current_by_method = data['current_by_method']
        self.breakers = data['breakers']
        self.total_center = data['total_center']
        self.total_current_ct = data['total_current_ct']
        self.total_active_power_ct = data['total_active_power_ct']
        self.total_reactive_power_ct = data['total_reactive_power_ct']
        self.total_apparent_power_ct = data['total_apparent_power_ct']
        self.total_fp = data['total_fp']
        self.name_impedance = data['name_impedance']
        self.elec_differencial = data['elect_differencial']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.tg_id = data['tg_id']
        self.td_id = data['td_id']

    
    @classmethod
    def get_all_circuits_by_user_id(cls, data):
        query = "SELECT *, proyects.name AS proyecto, tgs.name AS tg FROM loads LEFT JOIN circuits ON circuits.id = loads.circuit_id LEFT JOIN tgs ON tgs.id = circuits.tg_id \
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
        query = "SELECT *, loads.id, loads.length AS largo FROM loads LEFT JOIN circuits ON circuits.id = loads.circuit_id WHERE circuits.id = %(circuit_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        circuits = []
        if (not results):
            return []
        for ct in results:
            circuits.append(ct)
        return circuits

    @classmethod
    def detail_total_circuits_by_td_id(cls, data):
        query = "SELECT \
                    (SELECT name FROM total_tds WHERE total_tds.td_id = %(td_id)s)  AS name, \
                    (SELECT name FROM tds WHERE id = %(td_id)s AND tg_id = %(tg_id)s) AS ref, \
                    SUM(loads.qty) AS total_center, \
                    (SELECT id FROM tgs WHERE tgs.id = %(tg_id)s) AS tab_secondary, \
                    (SELECT id FROM tds WHERE tds.id = %(td_id)s) AS td_id, \
                    SUM(total_current) AS total_current_ct, \
                    SUM(total_active_power) AS total_active_power_ct, \
                    SUM(total_active_power) AS total_active_power_ct, \
                    SUM(total_reactive_power) AS total_reactive_power_ct,\
                    SUM(total_apparent_power) AS total_apparent_power_ct,\
                    ROUND(SUM(total_active_power) / SUM(total_apparent_power),2) AS all_fp,\
                    MAX(single_voltage) AS single_voltage \
        FROM circuits INNER JOIN loads ON circuits.id = loads.circuit_id INNER JOIN tds ON circuits.td_id = tds.id WHERE circuits.tg_id = %(tg_id)s AND circuits.td_id = %(td_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        circuits_td = []
        if (not results):
            return []
        for ct in results:
            circuits_td.append(ct)
        return circuits_td

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
        query = "INSERT INTO circuits (name, ref, method, type_circuit, single_voltage, vp, secctionmm2, conduit, wires, current_by_method, breakers, elect_differencial, total_center, total_current_ct, total_active_power_ct, total_length_ct, total_fp, name_impedance, created_at, updated_at, tg_id, td_id) VALUES \
                (%(name)s, %(ref)s, %(method)s, %(type_circuit)s, %(single_voltage)s, NULL,  NULL, NULL,%(wires)s, NULL, NULL, NULL, NULL, NULL, NULL, %(total_length_ct)s, %(total_fp)s, %(name_impedance)s, NOW(), NOW(), %(tg_id)s, %(td_id)s);"
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
        query = "UPDATE circuits SET \
        total_center = (SELECT SUM(qty) FROM loads WHERE circuit_id = %(circuit_id)s),\
        total_current_ct = (SELECT SUM(total_current) FROM loads WHERE circuit_id = %(circuit_id)s), \
        total_active_power_ct = (SELECT SUM(total_active_power) FROM loads WHERE circuit_id = %(circuit_id)s), \
        total_apparent_power_ct = (SELECT SUM(total_apparent_power) FROM loads WHERE circuit_id = %(circuit_id)s),\
        total_reactive_power_ct = (SELECT SUM(total_reactive_power) FROM loads WHERE circuit_id = %(circuit_id)s),\
        total_length_ct = ROUND((SELECT SUM(length) FROM loads WHERE circuit_id = %(circuit_id)s), 2) WHERE circuits.id = %(circuit_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result 
    
    @classmethod
    def new_total_fp(cls, data):
        query = "SELECT ROUND(SUM(circuits.total_active_power_ct) / SUM(circuits.total_apparent_power_ct),2) AS power_factor FROM circuits WHERE id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def update_total_fp(cls, data):
        query = "UPDATE circuits SET total_fp = %(new_total_fp)s WHERE id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def update_name_impedance(cls, data):
        query = "UPDATE circuits SET name_impedance = %(name_impedance)s WHERE id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def all_name_impedance(cls, data):
        query = "SELECT name_impedance FROM circuits WHERE td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result  

    @classmethod
    def delete_circuit_by_id(cls, data):
        query = "DELETE FROM circuits WHERE id = %(circuit_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def conduit_mono_normal(cls, data):
        query = "SELECT c3 FROM conduits WHERE nameconduit >= %(secctionmm2)s LIMIT 1;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def conduit_tri_normal(cls, data):
        query = "SELECT c5 FROM conduits WHERE nameconduit >= %(secctionmm2)s LIMIT 1;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def conduit_mono_subte(cls, data):
        query = "SELECT c3 FROM conduitsubte WHERE namesubte >= %(secctionmm2)s LIMIT 1;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def conduit_tri_subte(cls, data):
        query = "SELECT c5 FROM conduitsubte WHERE namesubte >= %(secctionmm2)s LIMIT 1;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def update_conduit(cls, data):
        query = "UPDATE circuits SET conduit = %(conduit)s WHERE circuits.id = %(circuit_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result