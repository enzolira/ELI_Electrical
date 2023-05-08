from flask import flash
from src.config.mysqlconnection import connectToMySQL

class Circuit:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.ref = data['ref']
        self.qty = data['qty']
        self.load = data['load']
        self.total_power = data['total_power']
        self.voltage = data['voltage']
        self.fp = data['fp']
        self.method = data['method']
        self.total_current = data['total_current']
        self.length = data['length']
        self.seccionmm2 = data['secctionmm2']
        self.wires = data['wires']
        self.current_by_method = data['current_by_method']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.tg_id = data['tg_id']
        self.td_id = data['td_id']


    @classmethod
    def add_circuit(cls,data):
        query = "INSERT INTO circuits (name, ref, qty, load, total_load, voltage, fp, total_current, length, secctionmm2, method, wires, current_by_method, created_at, updated_at, tg_id, td_id) \
                SELECT '%(name)s', '%(qty)s', '%(load)s', '%(total_load)s', '%(voltage)s', '%(fp)s', '%(total_current)s', '%(length)s', '%(secctionmm2)s', '%(method)s', '%(wires)s', '%(current_by_method)s', NOW(), NOW(), '%(tg_id)s', '%(td_id)s'\
                FROM dual WHERE NOT EXISTS ( SELECT 1 FROM circuits WHERE name = '%(name)s' AND tg_id = '%(tg_id)s' AND td_id = '%(td_id)s');"
        result = connectToMySQL(cls.db).query_db(query,data)
        return result

    # @classmethod
    # def methodds_wiresh07z(cls,scalmin,methods):
    #     query = "SELECT * FROM wiresh07z WHERE %(methods)s = %(scalmin)s;"
    #     result = connectToMySQL(cls.db).query_db(query,scalmin,methods)
    #     return result
    

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
