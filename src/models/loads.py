from flask import flash
from src.config.mysqlconnection import connectToMySQL

class Load:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.nameloads = data['nameloads']
        self.qty = data['qty']
        self.active_power = data['active_power']
        self.total_active_power = data['total_active_power']
        self.total_reactive_power = data['total_reactive_power']
        self.total_apparent_power = data['total_apparent_power']
        self.impedance = data['impedance']
        self.length = data['length']
        self.fp = data['fp']
        self.total_current = data['total_current']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.circuit_id = data['circuit_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO loads (nameloads, qty, active_power, total_active_power, total_reactive_power, total_apparent_power, impedance, length, total_current, fp, voltage, created_at, updated_at, circuit_id) VALUES (%(nameloads)s, %(qty)s, %(active_power)s, %(total_active_power)s, %(total_reactive_power)s, %(total_apparent_power)s, %(impedance)s, %(length)s, %(total_current)s, %(fp)s, %(voltage)s,NOW(), NOW(), %(circuit_id)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM loads WHERE loads.id = %(load_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def delete_load_by_circuit_id(cls, data):
        query = "DELETE FROM loads WHERE circuit_id = %(circuit_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def all_impedance(cls, data):
        query = "SELECT impedance FROM loads WHERE circuit_id = %(circuit_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result