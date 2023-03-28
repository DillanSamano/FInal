from flask import render_template,redirect,request,flash ,session
from flask_app.models.user_model import User
from flask_app.models.posts_model import Post
from flask_app.controllers.user_controller import User
from flask_app.models.comment_model import Comments
from flask_app import app

@app.route("/save_comments/<int:post_id>", methods=['post'])
def save_comment(post_id):
    if 'user_id' not in session:
            return redirect("/")
    data = {
        'users_id': session['user_id'],
        'post_id': post_id,
        'comment': request.form['comment']
    }
    Comments.save_comment(data)
    return redirect("/about")