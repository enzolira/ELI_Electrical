from flask import Flask
from src.config.mysqlconnection import connectToMySQL

class Total_tds:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.ref = data['ref']
        self.tab_secondary = data['tab_secondary']
        self.td_id = data['td_id']
        self.total_center = data['total_center']
        self.total_current_ct = data['total_current_ct']
        self.current_r = data['current_r']
        self.current_s = data['current_s']
        self.current_t = data['current_t']
        self.total_active_power_ct = data['total_active_power_ct']
        self.total_apparent_power_ct = data['total_apparent_power_ct']
        self.total_reactive_power_ct = data['total_reactive_power_ct']
        self.td_fp = data['td_fp']
        self.td_impedance = data['td_impedance']
        self.single_voltage = data['single_voltage']
        self.elect_differencial = data['elect_differencial']
        self.secctionmm2 = data['secctionmm2']
        self.method = data['method']
        self.wires = data['wires']
        self.current_by_method = data['current_by_method']
        self.type_circuit = data['type_circuit']
        self.vp = data['vp']
        self.breakers = data['breakers']
        self.conduit = data['conduit']
        self.created_at = data['created_at']
        self.update_at = data['update_at']

    @classmethod
    def summary_tds(cls, data):
        query = "INSERT INTO total_tds (name, ref, tab_secondary, total_center, total_current_ct, current_r, current_s, current_t, total_active_power_ct, total_apparent_power_ct, total_reactive_power_ct, td_fp, td_impedance, single_voltage, td_id, created_at, updated_at,\
                elect_differencial, secctionmm2, method, wires, current_by_method, type_circuit, vp, breakers, conduit, length_from_tg) \
                VALUES (%(name)s, %(ref)s, %(tab_secondary)s, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, %(td_id)s, NOW(), NOW(), NULL, NULL, %(method)s, %(wires)s, NULL, 'feeder', NULL, NULL, NULL, %(length_from_tg)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def get_all_total_tds(cls):
        query = "SELECT * FROM total_tds;"
        result = connectToMySQL(cls.db).query_db(query)
        return result
    
    @classmethod
    def get_all_total_tds_by_tg_id(cls, data):
        query = "SELECT * FROM total_tds WHERE tab_secondary = %(tab_secondary)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_rst_total_tds_by_tg_id(cls, data):
        query = "SELECT COUNT(current_r) AS R, COUNT(current_s) AS S, COUNT(current_t) AS T FROM total_tds WHERE tab_secondary = %(tab_secondary)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def update_total_tds(cls, data):
        query = "UPDATE \
                    total_tds SET \
                    total_center = %(total_center)s, \
                    total_current_ct = %(total_current_ct)s, \
                    total_active_power_ct = %(total_active_power_ct)s, \
                    total_apparent_power_ct = %(total_apparent_power_ct)s, \
                    total_reactive_power_ct = %(total_reactive_power_ct)s, \
                    td_fp = ROUND(total_active_power_ct / total_apparent_power_ct, 2), \
                    single_voltage = %(single_voltage)s WHERE td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def update_method_total_td(cls, data):
        query = "UPDATE total_tds SET current_by_method = %(current_by_method)s WHERE td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def update_secctionmm2_total_td(cls, data):
        query = "UPDATE total_tds SET secctionmm2 = %(secctionmm2)s WHERE td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def update_breakers_total_td(cls, data):
        query = "UPDATE total_tds SET breakers = %(breakers)s WHERE td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def update_elect_differencial_total_td(cls, data):
        query = "UPDATE total_tds SET elect_differencial = %(elect_differencial)s WHERE td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def update_conduit_total_td(cls, data):
        query = "UPDATE total_tds SET conduit = %(conduit)s WHERE td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def update_td_impedance(cls, data):
        query = "UPDATE total_tds SET td_impedance = %(td_impedance)s WHERE td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def update_vp_td(cls, data):
        query = "UPDATE total_tds SET vp = %(vp)s WHERE td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def edit_name_total(cls,data):
        query = "UPDATE total_tds SET ref = %(ref)s WHERE td_id = %(td_id)s"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def update_current_r_td(cls, data):
        query = "UPDATE total_tds SET current_r = %(current_r)s WHERE td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def update_current_s_td(cls, data):
        query = "UPDATE total_tds SET current_s = %(current_s)s WHERE td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def update_current_t_td(cls, data):
        query = "UPDATE total_tds SET current_t = %(current_t)s WHERE td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def name_total_tds(cls, data):
        query = "SELECT name, id, td_id FROM total_tds WHERE tab_secondary = %(tab_secondary)s ORDER BY name ASC;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def update_name_total_td(cls, data):
        query = "UPDATE total_tds SET name = %(name)s WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result