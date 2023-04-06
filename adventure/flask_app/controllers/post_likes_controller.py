from flask import render_template,redirect,request,flash ,session
# from flask_app.models.user_model import User
# from flask_app.models.posts_model import Post
from flask_app.controllers.posts_controller import Post
from flask_app.models.post_likes_model import PostLikes
from flask_app.controllers.user_controller import User
from flask_app.models.comment_model import Comments
from flask_app import app

@app.route('/save_post_likes/<int:post_id>', methods=['post'])
def like(post_id): 
    data = {
        'post_id': post_id,
    }
    PostLikes.save_post_like(data)
    return redirect("/about")