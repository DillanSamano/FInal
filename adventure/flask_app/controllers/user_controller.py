from flask import render_template,redirect,request,flash,session
from flask_app.models.user_model import User
from flask_app.models.adventure_model import Adventure
from flask_app.models.posts_model import Post

from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route('/')
def index():
    return render_template("register.html")



@app.route("/register", methods=["post"])
def create_user():
    if not User.user_validator(request.form):
        return redirect('/')
    if User.get_user_by_email(request.form):
        flash("email is already in use or your password and confirm no match")
        return redirect('/')
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'username':request.form['username'],
        'email':request.form['email'],
        'password':bcrypt.generate_password_hash(request.form['password'])
    }
    print(data['password'])
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect ("/menu")





@app.route("/login")
def show_login():
    return render_template("login.html")



@app.route("/login", methods=["post"])
def login():
    data = {'email': request.form['email']}
    user_in_db = User.get_user_by_email(data)
    if not user_in_db:
        flash("email or password is not correct")
        return redirect("/login")
    if not bcrypt.check_password_hash(user_in_db.password,request.form['password']):
        flash("email or password is not correct")
        return redirect("/login")
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")



@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect("/")
    return render_template("dashboard.html", user=User.get_user_by_id(session['user_id']))


@app.route("/menu")
def dashboard2():
    if 'user_id' not in session:
        return redirect("/")
    return render_template("reg_dashboard.html" ,user=User.get_user_by_id(session['user_id']))


@app.route("/about")
def about_page():
    if 'user_id' not in session:
        return redirect("/")
    all_posts = Post.get_all_with_creator()
    return render_template("abt.html",one_user = User.get_user_by_id(session['user_id']), all_posts = all_posts)



@app.route("/clear_session")
def clear():
    session.clear()
    return redirect("/")


@app.route('/Game_over')
def game_over():
    if 'user_id' not in session:
        return redirect("/")
    return render_template("game_over.html", user=User.get_user_by_id(session['user_id']))

@app.route("/add_topic")
def add_topic():
    if 'user_id' not in session:
        return redirect("/")
    return render_template('add_topic.html')




@app.route("/home")
def home():
        if session['health'] < 0:
            session['health'] += 100
        return render_template("1.html",user=User.get_user_by_id(session['user_id']),)

@app.route("/yes")
def run():
    return render_template("2.html", user=User.get_user_by_id(session['user_id']))

@app.route("/explain")
def explain():
    return render_template("2.5.html", user=User.get_user_by_id(session['user_id']))

@app.route("/explain/for_dummies")
def dum():
    return render_template("2.6.html", user=User.get_user_by_id(session['user_id']))

@app.route("/explain/for_dummies/explain_more!!")
def dumdum():
        session['health'] -= 5
        return render_template("2.7.html", user=User.get_user_by_id(session['user_id']))

@app.route("/ok")
def gotIt():
    return render_template('3.html',user=User.get_user_by_id(session['user_id']))


@app.route("/city")
def city():
    return render_template('3.5.html',user=User.get_user_by_id(session['user_id']))

@app.route("/accept")
def accept_milk():
    session['health'] += 5 
    return render_template('accept.html',user=User.get_user_by_id(session['user_id']))



@app.route("/intoTheCity")
def intoTheCity():
    return render_template('intoTheCity.html',user=User.get_user_by_id(session['user_id']))

@app.route("/Explore")
def exp():
    return render_template('4.html',user=User.get_user_by_id(session['user_id']))

@app.route("/END/DEMO")
def demo():
    return render_template('END.html',user=User.get_user_by_id(session['user_id']))


@app.route("/right")
def right():
    session['health'] -= 100
    return render_template('5.html',user=User.get_user_by_id(session['user_id']))




@app.route("/acceptance")
def accept():
    if session['health'] > 10:
        True
    elif session['health'] < 10 :
        return redirect('/Game_over')
    return render_template('6.html',user=User.get_user_by_id(session['user_id']))



# @app.route("/fight")
# def fight():
#     session['health'] -= 20
#     if session['health'] > 10:
#         True
#     elif session['health'] < 10 :
#         return redirect('/Game_over')
#     return render_template('6.html',user=User.get_user_by_id(session['user_id']))

# @app.route("/fight")
# def ():
#     session['health'] -= 10
#     if session['health'] > 10:
#         True
#     elif session['health'] < 10 :
#         return redirect('/Game_over')
#     return render_template("2.html", user=User.get_user_by_id(session['user_id']))