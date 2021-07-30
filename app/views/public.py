from flask import render_template, redirect
from app.views import views_blueprint
from utilities import get_language_dictionary

@views_blueprint.route('/')
@views_blueprint.route('/home.html')
def home():
    return home_2021_fr()

@views_blueprint.route('/2021/en/home.html')
def home_2021_en():
    language="en"
    d=get_language_dictionary(language)
    return render_template(language+"/home.html",
                           year=2021,
                           language=d,
                           title="Meteohack",
                           banner_index=1)

@views_blueprint.route('/2021/fr/home.html')
def home_2021_fr():
    language="fr"
    d=get_language_dictionary(language)
    return render_template(language+"/home.html",
                           year=2021,
                           language=d,
                           title="Meteohack",
                           banner_index=1)
    
@views_blueprint.route('/2021/en/faq.html')
def faq_2021_en():
    language="en"
    d=get_language_dictionary(language)
    return render_template(language+"/faq.html",
                           year=2021,
                           language=d,
                           title="Meteohack - FAQ",
                           banner_index=1)

@views_blueprint.route('/2021/fr/faq.html')
def faq_2021_fr():
    language="fr"
    d=get_language_dictionary(language)
    return render_template(language+"/faq.html",
                           year=2021,
                           language=d,
                           title="Meteohack - FAQ",
                           banner_index=1)