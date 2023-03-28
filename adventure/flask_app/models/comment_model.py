from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask import flash
import pprint
import re

db = "user_n_adventure"

class Comments : 
    def __init__(self,data):
        self.users_id = data['users_id']
        self.posts_id = data['posts_id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

def save_comment(cls,data):
    query = ' INSERT INTO comments (users_id,post_id,comment) VALUES (%(users_id)s,%(post_id)s,%(comment)s,)'
    return connectToMySQL(db).query_db(query,data)