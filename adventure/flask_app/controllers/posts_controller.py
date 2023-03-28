from flask import render_template,redirect,request,flash ,session
from flask_app.models.user_model import User
from flask_app.models.posts_model import Post
from flask_app.controllers.user_controller import User
from flask_app import app



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
    return render_template("show.html", one_user = User.get_single_post(data))