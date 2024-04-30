from flask import flash
from src.config.mysqlconnection import connectToMySQL

class Jobs:
    db = "ELI_ELECTRICAL"
    def __init__(self,data):
        self.id = data['id']
        self.proyect_id = data['proyect_id']
        self.title = data['title']
        self.description = data['description']
        self.start = data['start']
        self.end = data['end']
        self.created_at = data['created_at']
        self.update_at = data['update_at']

    @classmethod
    def add_event(cls,data):
        query = "INSERT INTO jobs (title, user_id, proyect_id, description, start, end, created_at, update_at) VALUES (%(title)s, %(user_id)s, %(proyect_id)s, %(description)s, %(start)s, %(end)s, NOW(), NOW());"
        result = connectToMySQL(cls.db).query_db(query,data)
        print(result)
        return result
    
    @classmethod
    def get_all_jobs_by_user_id(cls,data):
        query = "SELECT * FROM jobs WHERE user_id = %(id)s"
        result = connectToMySQL(cls.db).query_db(query,data)
        jobs = []
        for job in result:
            jobs.append(job)
        return jobs
    
    @classmethod
    def get_all_jobs_by_proyect_id(cls,data):
        query = "SELECT * FROM jobs INNER JOIN proyects ON jobs.proyect_id = proyects.id WHERE proyects.id = %(proyect_id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        job = []
        for xl in result:
            job.append(xl)
        return job
    
    @classmethod
    def jobs_by_proyect_id(cls,data):
        query = "SELECT title, description, start, end, proyect_id FROM jobs WHERE proyect_id = %(proyect_id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        jobs = []
        for xl in result:
            jobs.append(xl)
        return jobs