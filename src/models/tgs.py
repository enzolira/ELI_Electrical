from flask import Flask, flash
from src.config.mysqlconnection import connectToMySQL

class Tgs:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.tag = data['tag']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.proyect_id = data['proyect_id']


    @classmethod
    def add_tgs(cls,data):
        query = "INSERT INTO tgs (name, tag,created_at, updated_at, proyect_id) VALUES (%(name)s, %(tag)s, NOW(), NOW(), %(proyect_id)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def all_circuits_by_tg(cls,data):
        query = "SELECT * FROM circuits WHERE circuits.tg_id = %(tg_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_tds_tgs_circuit(cls,data):
        query = "SELECT COUNT(*) + (SELECT COUNT(*) FROM tds WHERE tds.tg_id = %(tg_id)s) AS circuits_tg FROM circuits WHERE circuits.tg_id = %(tg_id)s AND circuits.td_id IS NULL;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_tgs_circuit_tds_null(cls,data):
        query = "SELECT * FROM circuits WHERE circuits.tg_id = %(tg_id)s AND circuits.td_id IS NULL;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def count_tds(cls,data):
        query = "SELECT COUNT(*) AS circ_td FROM tds WHERE tds.tg_id = %(tg_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def get_tgs_by_project(cls,data):
        query = "SELECT * FROM tgs WHERE proyect_id = %(proyect_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if (not result):
            return []
        tgs = []
        for elmt in result:
            tgs.append(elmt)
        return tgs
# -----
    @classmethod
    def get_all_circuits_by_tg_id(cls,data):
        query = "SELECT COUNT(*) + 1 AS new_circuit_tg FROM circuits WHERE circuits.tg_id = %(tg_id)s AND circuits.td_id is NULL;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if (not result):
            return []
        tgs_circuit = []
        for elmt in result:
            tgs_circuit.append(elmt)
        return tgs_circuit

    @classmethod
    def get_tgs_and_tds_by_project(cls,data):
        query = "SELECT *, tgs.id AS tgid, tgs.name AS tg, tds.id AS tdid, tds.name AS td FROM tgs LEFT JOIN tds ON tgs.id = tds.tg_id LEFT JOIN proyects ON proyects.id = tgs.proyect_id WHERE proyects.id = %(proyect_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        if (not result):
            return []
        tgs = []
        for elmt in result:
            tgs.append(elmt)
        return tgs

    @classmethod
    def delete_load_by_tgId(cls,data):
        query = "DELETE loads FROM loads JOIN circuits ON loads.circuit_id = circuits.id WHERE circuits.tg_id = %(tg_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def delete_circuits_by_tgId(cls,data):
        query = "DELETE FROM circuits WHERE tg_id = %(tg_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def delete_tds_by_tgId(cls,data):
        query = "DELETE FROM tds WHERE tg_id = %(tg_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def delete_tgs_by_tgId(cls,data):
        query = "DELETE FROM tgs WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def delete_total_tgs_by_tgId(cls,data):
        query = "DELETE FROM total_tds WHERE total_tds.tab_secondary = %(tab_secondary)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def name_tg(cls,data):
        query = "SELECT name FROM tgs WHERE id = %(tg_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def total_name_tg(cls,data):
        query = "SELECT name, id FROM circuits WHERE tg_id = %(tg_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @classmethod
    def update_name(cls,data):
        query = "UPDATE circuits SET name = %(name)s WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def tg_id_by_circuit(cls,data):
        query = "SELECT tg_id FROM circuits WHERE id = %(circuit_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result 

# -------------- excel total_tgs ----------------------
    @classmethod
    def detail_to_excel(cls,data):
        query = "SELECT \
                    CAST(name AS SIGNED) AS Circuito, ref AS Carga, total_center AS 'Cantidad', CAST((total_active_power_ct / total_center) * 1000 AS SIGNED) AS 'Potencia por Carga [W]', \
                    CASE WHEN name_impedance = 'capacitance' THEN 'Capacitiva' ELSE 'Inductiva' END AS 'Impedancia', REPLACE(total_fp, '.', ',') AS 'Fp', 50 AS 'Frecuencia [Hz]', REPLACE(total_active_power_ct, '.', ',') AS 'Potencia Total [Kw]', \
                    REPLACE(current_r, '.', ',') AS 'R [A]', REPLACE(current_s, '.', ',') AS 'S [A]', REPLACE(current_t, '.', ',') AS 'T [A]', \
                    CASE WHEN single_voltage = 0.220 THEN 220 ELSE 380 END AS 'Tensión [V]', CAST(total_length_ct AS SIGNED) AS 'Largo [m]', REPLACE(vp, '.', ',') AS 'Vp [V]', UPPER(method) AS 'Tipo de Instalación', wires AS 'Tipo de Aislación', REPLACE(secctionmm2, '.', ',') AS 'Conductor [mm2]', CAST(conduit AS SIGNED) AS 'Canalización [mm]', \
                    breakers AS 'Disyuntor', elect_differencial AS 'Protección Diferencial' FROM circuits WHERE tg_id = %(tg_id)s AND td_id IS NULL \
                    UNION ALL \
                SELECT \
                    CAST(name AS SIGNED) AS Nombre, ref AS Carga, total_center AS 'Cantidad', CAST((total_active_power_ct / total_center) * 1000 AS SIGNED) AS 'Potencia por Carga [W]', \
                    CASE WHEN td_impedance = 'capacitance' THEN 'Capacitiva' ELSE 'Inductiva' END AS 'Impedancia', REPLACE(td_fp, '.', ',') AS 'Fp', 50 AS 'Frecuencia [Hz]', REPLACE(total_active_power_ct, '.', ',') AS 'Potencia Total [Kw]', \
                    REPLACE(current_r, '.', ',') AS 'R [A]', REPLACE(current_s, '.', ',') AS 'S [A]', REPLACE(current_t, '.', ',') AS 'T [A]', \
                    CASE WHEN single_voltage = 0.220 THEN 220 ELSE 380 END AS 'Tensión [V]', CAST(length_from_tg AS SIGNED) AS 'Largo [m]', REPLACE(vp, '.', ',') AS 'Vp [V]', UPPER(method) AS 'Tipo de Instalación', wires AS 'Tipo de Aislación', REPLACE(secctionmm2, '.', ',') AS 'Conductor [mm2]', CAST(conduit AS SIGNED) AS 'Canalización [mm]', \
                    breakers AS 'Disyuntor', elect_differencial AS 'Protección Diferencial'\
                    FROM total_tds WHERE tab_secondary = %(tg_id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def edit_name(cls,data):
        query = "UPDATE tgs SET name = %(name)s , tag = %(tag)s WHERE id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result
    
    @staticmethod
    def validate_new_tg(tg):
        is_valid = True
        if not tg.get("name"):
            flash("Ingresa nombre del Tablero General", "new_tg")
            is_valid = False
        elif tg.get("proyect_id") == "-Seleccione proyecto-":
            flash("Selecciona un Proyecto", "new_tg")
            is_valid = False
        elif not tg.get("tag"):
            flash("Ingresa identificación del Tablero", "new_tg")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_edit(tg):
        is_valid = True
        if not tg.get("name"):
            flash("Ingresa el nuevo nombre del Tablero General", "error_edit_tg")
            is_valid = False
        elif not tg.get("tag"):
            flash("Ingresa la nueva identificación del Tablero", "error_edit_tg")
            is_valid = False
        return is_valid

    @classmethod
    def sum_all_current(cls, tg_id):
        query = "SELECT SUM(current_r) AS R, SUM(current_s) AS S, SUM(current_t) AS T FROM circuits WHERE tg_id  = %(tg_id)s;"
        result = connectToMySQL(cls.db).query_db(query, tg_id)
        return result