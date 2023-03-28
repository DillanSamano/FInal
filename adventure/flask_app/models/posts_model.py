from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask import flash
import pprint
import re

db = "users_n_adventure"

class Post : 
    def __init__(self,data):
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.id = data['id']
        self.creator = None


    @classmethod
    def save_post(cls,data):
        query = 'INSERT INTO posts (user_id,content) VALUES ( %(id)s, %(content)s )'
        return connectToMySQL(db).query_db(query,data) 
    

    @classmethod
    def get_all_with_creator(cls):
        query = "SELECT * FROM paintings LEFT JOIN users ON users.id = paintings.user_id "
        results = connectToMySQL(db).query_db(query)
        all_paintings = []
        pprint.pprint(results)
        for p in results:
            paint = cls(p)
            user_data = {
                'id': p['users.id'],
                'first_name': p['first_name'],
                'last_name' : p['last_name'],
                'email' :  p['email'],
                'password' : p['password'],
                'created_at' : p['users.created_at'],
                'updated_at' : p['users.updated_at']
            }
            paint.creator = user_model.User(user_data)
            all_paintings.append(paint)
        return all_paintings
    

    @classmethod
    def update_post(cls,data,id):
        query = f'''
        UPDATE posts
        set content = %(content)s
        WHERE id = {id}
        '''
        return connectToMySQL(db).query_db(query,data)




    @classmethod
    def delete_post(cls,id):
        query = f"DELETE FROM posts where id = {id}"
        return connectToMySQL(db).query_db(query)



    @staticmethod
    def post_validator(paintings):
        is_valid = True

        if len(paintings['price']) < 0:
                flash("price cannont be left blank")
                is_valid = False


        return is_valid
