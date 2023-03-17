from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask import flash
import pprint
import re
import os

db = "user_n_adventure"

class Adventure : 
    def __init__(self,data):
        self.page = data['page']
        self.health = data['health']
        self.character = data['character']
        self.inventory = data['inventory']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.id = data['id']


    @classmethod
    def create_adventure(cls,data):
        query = 'INSERT INTO adventure (page,health,character_name,inventory,user_id) VALUES (%(page)s,%(health)s,%(character)s,%(inventory)s, %(id)s)'
        return connectToMySQL(db).query_db(query,data)








    @staticmethod
    def adventure_validator(adventure):
        is_valid = True 
        if len(adventure['first_name']) < 6:
            flash("your name is not long enough!")
            is_valid = False


        return is_valid











