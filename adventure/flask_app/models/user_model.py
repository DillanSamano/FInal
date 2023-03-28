from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.adventure_model import Adventure
import pprint
from flask import flash
import re 
import os

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASWORD_REGEX = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-])$')

db = "user_n_adventure"

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posts = []
        self.adventure = []
        self.ad=[]

    @classmethod
    def get_single_post(cls,data):
        query = "SELECT * FROM users left join posts ON posts.user_id = users.id where posts.id =%(id)s"
        results = connectToMySQL(db).query_db(query,data)
        pprint.pprint(results, sort_dicts=False)
        user = cls(results[0])
        for posts in results: 
            posts_dictionary = {
                'id': posts['posts.id'],
                'content' : posts['content'],
                'created_at' : posts['created_at'],
                'updated_at' : posts['updated_at']
            }
            user.posts.append(User(posts_dictionary))
        return user
    


    @classmethod
    def get_single_adventure(cls,data):
        query = "SELECT * FROM adventure left join users ON adventure.user_id = users.id where user_id=  %(id)s"
        results = connectToMySQL(db).query_db(query,data)
        pprint.pprint(results, sort_dicts=False)
        user = cls(results[0])
        for ad in results: 
            ad_dictionary = {
                'id': ad['id'],
                'page' : ad['page'],
                'health' : ad['health'],
                'character_name' : ad['character_name'],
                'inventory' : ad['inventory'],
                'created_at' : ad['created_at'],
                'updated_at' : ad['updated_at']

            }
            user.ad.append(Adventure(ad_dictionary))
        return user
    


    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,username,password) VALUES (%(first_name)s, %(last_name)s,%(email)s,%(username)s,%(password)s)"
        return connectToMySQL(db).query_db(query,data)



    @classmethod
    def get_user_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(db).query_db(query,data)
        print(results)
        if len(results) < 1:
            return False
        return cls(results[0])
    


    @classmethod
    def get_user_with_adventure(cls,data):
        query = "SELECT * FROM adventure left join users ON adventure.user_id = users.id where users.id = %(id)s"
        results = connectToMySQL(db).query_db(query,data)
        pprint.pprint(results, sort_dicts=False)




    @classmethod
    def get_user_by_id(cls,id):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(db).query_db(query,{'id':id})
        print(results)
        if len(results) < 0:
            return False
        return cls(results[0])







    # def reduce_health(self):
    #         self.health = self.health - 10
    #         if self.health <= 0 :






















    @staticmethod
    def user_validator(user):
        is_valid = True 
        if len(user['first_name']) < 6:
            flash("your name is not long enough!")
            is_valid = False

        if len(user['last_name']) < 4:
            flash("your last name is not long enough")
            is_valid = False
            

        if len(user['username']) < 4:
            flash("your username is not long enough")
            is_valid = False

        if not EMAIL_REGEX.match(user['email']):
            flash("your email invalid!")
            is_valid = False

        if len(user['password']) < 8:
            if not PASWORD_REGEX.match(user['password']):
                flash("your password is invalid!, must have 1 uppercase, 1 lowercase, 1 digit, 1 specail character must be 8 characters or longer")
                is_valid = False

        if not user ['password'] == user['cpass']:
            flash("password and confirm password do not match")
            is_valid = False

        return is_valid
