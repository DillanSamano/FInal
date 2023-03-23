from flask import render_template,redirect,request,flash ,session
from flask_app.models.user_model import User
# from flask_app.controllers.user_controller import User
from flask_app.models.adventure_model import Adventure
from flask_app import app


@app.route("/Character_menu")
def character_menu():
    if 'user_id' not in session:
            return redirect("/")
    return render_template("character.html")



@app.route("/create_adventure", methods=['post'])
def create_Character():
    if 'user_id' not in session:
        return redirect("/")
    data = {
        'page' : request.form['page'],
        'character' : request.form['character'],
        'inventory' : request.form['inventory'],
        'id': session['user_id'],
    }
    session['health'] = int(request.form['health'])
    Adventure.create_adventure(data)
    return redirect("/home")


@app.route("/continue")
def continue_adventure():
    return redirect("/home")


