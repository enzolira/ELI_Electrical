from flask import flash
from src.config.mysqlconnection import connectToMySQL

class Load:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.qty = data['qty']
        self.power = data['power']
        self.total_power = data['total_power']
        self.total_current = data['total_current']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.circuit_id = data['circuit_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO loads (qty, power, total_power, total_current, created_at, updated_at, circuit_id) VALUES (%(qty)s, %(power)s, ((" + data.get('qty') + " * " + data.get('power') + ")/1000), ROUND(((" + data.get('qty') + " * " + data.get('power') + ")/1000)/" + data.get('single_voltage') + ",2), NOW(), NOW(), %(circuit_id)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result