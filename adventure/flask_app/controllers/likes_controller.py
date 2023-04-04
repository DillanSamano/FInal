from flask import render_template,redirect,request,flash ,session
# from flask_app.models.user_model import User
# from flask_app.models.posts_model import Post
# from flask_app.controllers.user_controller import User
from flask_app.models.likes_model import Likes
# from flask_app.models.comment_model import Comments
from flask_app import app


# @app.route('/post')
# def index():
#     like += 1
#     return redirect(post)