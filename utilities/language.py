
def get_language_dictionary(language):
    """
    Given 'en' or 'fr' returns a dictionary:
    
    {"label":"English",
     "other_label":"Francais",
     "iso":"en",
     "other_iso":"fr"}
    """
    
    other="en" if language=="fr" else "fr"
    labels={"en":"English",
            "fr":"Français"}
    return {"label":labels[language],
            "other_label":labels[other],
            "iso":language,
            "other_iso":other}