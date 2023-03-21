from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from flask_app.controllers import user_controller 
from flask import flash
import pprint
import re

db = "user_n_adventure"

class Adventure : 
    def __init__(self,data):
        self.page = data['page']
        self.health = data['health']
        self.character_name = data['character_name']
        self.inventory = data['inventory']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.id = data['id']


    @classmethod
    def create_adventure(cls,data):
        query = 'INSERT INTO adventure (page,health,character_name,inventory,user_id) VALUES (%(page)s,%(health)s,%(character)s,%(inventory)s, %(id)s)'
        return connectToMySQL(db).query_db(query,data)



    @classmethod
    def save(cls,data):
        query = 'INSERT INTO adventure (page,health,inventory,user_id) VALUES (%(page)s,%(health)s,%(inventory)s, %(id)s)'
        return connectToMySQL(db).query_db(query,data)


    @classmethod
    def health(cls,data):
        query = "SELECT health FROM users JOIN adventure ON adventure.user_id = users.id where user_id  = %(id)s"
        results = connectToMySQL(db).query_db(query,data)
        print(results)









