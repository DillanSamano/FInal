from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user_model import User
from flask import flash
import pprint
import re

db = "user_n_adventure"

class Comments : 
    def __init__(self,data):
        self.users_id = data['users_id']
        self.post_id = data['post_id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None
        self.poster = None

    @classmethod
    def save_comment(cls,data):
        query = 'INSERT INTO comments (users_id,post_id,comment) VALUES (%(users_id)s,%(post_id)s,%(comment)s)'
        return connectToMySQL(db).query_db(query,data)
    


    @classmethod
    def display_comments(cls):
        query = '''SELECT * FROM posts 
            LEFT JOIN comments ON comments.post_id = posts.id
            LEFT JOIN users ON comments.users_id = users.id;'''
        results = connectToMySQL(db).query_db(query)
        all_comments = []
        for row_in_db in results:
            comment_data={
            'users_id' : row_in_db['users_id'],
            'post_id' : row_in_db['post_id'],
            'comment' : row_in_db['comment'],
            'created_at' : row_in_db['created_at'],
            'updated_at' : row_in_db['updated_at'],
            }
            user_data = {
            'id' : row_in_db['users.id'],
            'first_name' : row_in_db['first_name'],
            'last_name' : row_in_db['last_name'],   
            'username' :row_in_db['username'],
            'email' : row_in_db['email'],
            'password' : row_in_db['password'],
            'created_at' :row_in_db['users.created_at'],
            'updated_at' : row_in_db['users.updated_at'],
            }
            comment = cls(comment_data)
            comment.poster = User(user_data)
            all_comments.append(comment)
        return all_comments
    


    