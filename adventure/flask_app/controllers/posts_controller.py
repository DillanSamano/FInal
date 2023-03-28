from flask import render_template,redirect,request,flash ,session
from flask_app.models.user_model import User
from flask_app.models.posts_model import Post
from flask_app.controllers.user_controller import User
from flask_app import app



@app.route("/new_topic", methods=['post'])
def create_painting():
    if not Post.post_validator(request.form):
        return redirect("/new_topic")
    data = {
        'content' : request.form['content'],
        'id': session['user_id']
    }
    Post.save_post(data)
    return redirect("/about")

