from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask_app.controllers import likes_controller 
from flask import flash
import pprint

db = "user_n_adventure"

class Likes: 
    def __init__(self,data):
        self.content = data['likes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.id = data['id']
        self.creator = None



    @classmethod
    def save_like(cls,data):
        query = 'INSERT INTO posts (user_id,likes) VALUES ( %(id)s, %(likes)s )'
        return connectToMySQL(db).query_db(query,data) 
    

    @classmethod
    def update_post(cls,data,id):
        query = f'''
        UPDATE posts
        set content = %(content)s
        WHERE id = {id}
        '''
        return connectToMySQL(db).query_db(query,data)

