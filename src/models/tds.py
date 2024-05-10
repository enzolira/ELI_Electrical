from flask import Flask
from src.config.mysqlconnection import connectToMySQL

class Tds:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.tg_id = data['tg_id']
        self.name = data['name']
        self.tag = data['tag']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_tds(cls, data):
        query = "INSERT INTO tds (tg_id, name, tag, created_at, updated_at) VALUES (%(tg_id)s, %(name)s, %(tag)s, NOW(), NOW())"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def get_td_by_id(cls, data):
        query = "SELECT * FROM tds WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_all_tds_by_tg_id(cls, data):
        query = "SELECT * FROM tds WHERE tg_id = " + str(data.get('tg_id')) + ";"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        if (not results):
            return []
        tds = []
        for i in results:
            tds.append(i)
            print(tds)
        return tds

    @classmethod
    def get_all_circuits_by_td_id_and_tg_id(cls,data):
        query = "SELECT COUNT(*) + 1 AS new_circuit_td FROM circuits WHERE circuits.td_id = %(td_id)s AND circuits.tg_id = %(tg_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if (not result):
            return []
        tds_circuit = []
        for elmt in result:
            tds_circuit.append(elmt)
        return tds_circuit


    @classmethod
    def summary_circuits_tds(cls, data):
        query = "SELECT *, tds.name AS nombre FROM circuits INNER JOIN tds ON circuits.td_id = tds.id WHERE circuits.td_id = %(td_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        if (not results):
            return []
        tds = []
        for i in results:
            tds.append(i)
            print(tds)
        return tds
    
    @classmethod
    def delete_load_by_tdId(cls,data):
        query = "DELETE loads FROM loads JOIN circuits ON loads.circuit_id = circuits.id WHERE circuits.td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def delete_circuits_by_tdId(cls,data):
        query = "DELETE FROM circuits WHERE td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def delete_tds_by_tdId(cls,data):
        query = "DELETE FROM tds WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def delete_total_tds_by_tdId(cls,data):
        query = "DELETE FROM total_tds WHERE total_tds.td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

#  ------ excel total_tds ---------
    @classmethod
    def detail_to_excel(cls,data):
        query = query = "SELECT \
                            ref AS Nombre, \
                            total_center AS 'Cantidad de cargas', \
                            CAST((total_active_power_ct / total_center) * 1000 AS SIGNED) AS 'Potencia por carga [W]', \
                            total_active_power_ct AS 'Potencia total [Kw]', \
                            CASE WHEN name_impedance = 'capacitance' THEN 'Capacitiva' ELSE 'Inductiva' END AS 'Impedancia', \
                            total_fp AS 'Fp', \
                            50 AS 'Frecuencia [Hz]', \
                            CASE WHEN single_voltage = 0.220 THEN 220 ELSE 380 END AS 'Tensión [V]', \
                            total_current_ct AS 'Intensidad total [A]', \
                            total_length_ct AS 'Largo [m]', \
                            vp AS 'Vp [V]' , \
                            UPPER(method) AS 'Tipo de instalación', \
                            wires AS 'Tipo de Aislación', \
                            secctionmm2 AS 'Conductor [mm2]', \
                            CAST(conduit AS SIGNED) AS 'Canalización [mm]', \
                            breakers AS 'Disyuntor', \
                            elect_differencial AS 'Protección Diferencial'\
                            FROM circuits WHERE circuits.td_id = %(td_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
#  --------------------------------

    @classmethod
    def edit_name(cls,data):
        query = "UPDATE tds SET name = %(name)s , tag = %(tag)s WHERE id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result