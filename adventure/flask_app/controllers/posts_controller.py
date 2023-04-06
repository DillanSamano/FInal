from flask import render_template,redirect,request,flash ,session
from flask_app.models.user_model import User
from flask_app.models.posts_model import Post
from flask_app.controllers.user_controller import User
from flask_app.models.comment_model import Comments
from flask_app.controllers.post_likes_controller import PostLikes
from flask_app import app
import js2py



@app.route("/add_topic", methods=['post'])
def create_topic():
    if 'user_id' not in session:
            return redirect("/")
    if not Post.post_validator(request.form):
        return redirect("/add_topic")
    data = {
        'content' : request.form['content'],
        'id': session['user_id']
    }
    Post.save_post(data)
    return redirect("/about")

@app.route("/show_post/<int:id>")
def show_one_mag(id):
    print(id)
    data = {
        'id' : id
    }
    comments = Comments.display_comments()
    return render_template("show_post.html", one_user = User.get_single_post(data), comments = comments,    postlike = PostLikes.get_post_likes(data))




@app.route("/edit_post/<int:id>")
def show_user_edit(id):
    print(id)
    data = {
        'id' : id
    }
    return render_template("update_post.html", one_user = User.get_single_post(data))


@app.route("/update_post/<int:id>", methods = ['post'])
def updateD_post(id):
    Post.update_post(request.form,id)
    return redirect("/about")

@app.route("/delete/<int:id>")
def delete_user_post(id):
    Post.delete_post(id)
    return redirect("/about")


