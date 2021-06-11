from flask import render_template
from app.views import views_blueprint

@views_blueprint.route('/')
@views_blueprint.route('/home')
def home():
    return render_template("home.html",
                           title="Meteohack")
    
@views_blueprint.route('/faq')
def event():
    return render_template("faq.html",title="Meteohack FAQ")
