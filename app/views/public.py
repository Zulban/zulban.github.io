from flask import render_template
from app.views import views_blueprint

@views_blueprint.route('/')
@views_blueprint.route('/home')
@views_blueprint.route('/home.html')
def home():
    return render_template("home.html",
                           title="Meteohack",
                           banner_index=1)

@views_blueprint.route('/faq')    
@views_blueprint.route('/faq.html')
def faq():
    return render_template("faq.html",
                           title="Meteohack FAQ",
                           banner_index=2)
