from flask import render_template, redirect
from app.views import views_blueprint
from utilities import get_language_dictionary

@views_blueprint.route('/')
@views_blueprint.route('/home.html')
def home():
    return home_2021("fr")

@views_blueprint.route('/2021/<language>/home.html')
def home_2021(language):
    d=get_language_dictionary(language)
    return render_template(language+"/home.html",
                           year=2021,
                           language=d,
                           title="Meteohack",
                           banner_index=1)

@views_blueprint.route('/2021/<language>/faq')
@views_blueprint.route('/2021/<language>/faq.html')
def faq_2021(language):
    d=get_language_dictionary(language)
    return render_template(language+"/faq.html",
                           year=2021,
                           language=d,
                           title="Meteohack - FAQ",
                           banner_index=1)

@views_blueprint.route('/2021/<language>/mentors')
@views_blueprint.route('/2021/<language>/mentors.html')
def mentors_2021(language):
    d=get_language_dictionary(language)
    return render_template(language+"/mentors.html",
                           year=2021,
                           language=d,
                           title="Meteohack - Mentors",
                           banner_index=1)
