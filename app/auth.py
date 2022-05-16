from flask import Blueprint

auth = Blueprint("auth",__name__)


@auth.route("/login")
def login():
    return "Login"




@auth.route("/Sign-up")
def login():
    return "Login"



@auth.route("/logout")
def login():
    return "Login"