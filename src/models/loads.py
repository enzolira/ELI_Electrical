from flask import flash
from src.config.mysqlconnection import connectToMySQL

class Load:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.nameloads = data['nameloads']
        self.qty = data['qty']
        self.power = data['power']
        self.total_power = data['total_power']
        self.single_voltage = data['single_voltage']
        self.fp = data['fp']
        self.total_current = data['total_current']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.circuit_id = data['circuit_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO loads (nameloads, qty, power, total_power, total_current, single_voltage, fp ,created_at, updated_at, circuit_id) VALUES (%(nameloads)s, %(qty)s, %(power)s, %(total_power)s, %(total_current)s, %(single_voltage)s, %(fp)s, NOW(), NOW(), %(circuit_id)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result