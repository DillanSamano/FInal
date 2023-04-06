from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import user_model
# from flask_app.controllers import likes_controller 
from flask import flash
import pprint

db = "user_n_adventure"

class Likes: 
    def __init__(self,data):
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.comments_id = data['comments_id']
        self.comments_post_id = data['comments_post_id']
        self.comments_post_id = data['comments_users_id']
        self.id = data['id']
        self.creator = None



    @classmethod
    def save_like(cls,data):
        query = 'insert into comment_likes (comments_users_id,comments_post_id,comments_id) VALUES (%(comments_users_id)s,%(comments_post_id)s,%(comments_id)s)'
        return connectToMySQL(db).query_db(query,data) 


    @classmethod
    def update_post(cls,data,id):
        query = f'''
        UPDATE posts
        set content = %(content)s
        WHERE id = {id}
        '''
        return connectToMySQL(db).query_db(query,data)

