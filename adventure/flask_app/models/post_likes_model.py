from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models import user_model
# from flask_app.controllers import likes_controller 
from flask import flash
import pprint

db = "user_n_adventure"

class PostLikes: 
    def __init__(self,data):
        self.id = data['id']
        self.creator = None
        self.postlike = []
        self.like = []




    @classmethod
    def save_post_like(cls,data):
        query = 'insert into post_likes (posts_id) VALUES (%(post_id)s)'
        return connectToMySQL(db).query_db(query,data) 


    @classmethod
    def update_post(cls,data,id):
        query = f'''
        UPDATE posts
        set content = %(content)s
        WHERE id = {id}
        '''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_post_likes(cls,data):
        query = "SELECT * FROM post_likes join posts ON posts_id = posts.id where posts.id =%(id)s"
        results = connectToMySQL(db).query_db(query,data)
        pprint.pprint(results, sort_dicts=False)
        likes = cls(results[0])
        for postlike in results: 
            postlike_dictionary = {
                'id': postlike['id'],
                # 'post_id': postlike['post_id'],
                # 'comments_id' : postlike['comment_id'],
            }
            likes.postlike.append(PostLikes(postlike_dictionary))
        return likes
    