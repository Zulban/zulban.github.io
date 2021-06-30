#!venv/bin/python3

"""Meteohack CLI

Run the meteohack as a Flask web app, or generate static web files.

Usage:
    meteohack web [options]
    meteohack freeze [options]
   
Options:
    --host=<host>         Host. [default: localhost]
    --port=<port>         Port. [default: 5000]
    --freeze=<folder>     Folder to dump all the static files for freeze. [default: build]
    
    -h --help             Show this screen.
    -v --version          Show version.
"""

from app import create_app
from utilities import docopt
from constants import PROJECT_ROOT
from flask_frozen import Freezer

def main(args):
    
    app=create_app()
        
    if args["web"]:
        
        app.run(host=args["--host"],
                port=int(args["--port"]),
                threaded=True)        
    
    elif args["freeze"]:
        app.config["FREEZER_IGNORE_MIMETYPE_WARNINGS"]=True
        app.config["FREEZER_DESTINATION"]=args["--freeze"]
        freezer = Freezer(app)
        freezer.freeze()
        build_folder=PROJECT_ROOT+"app/build/"
        print("Froze Flask app: "+build_folder)
    
    print("Done.")

if __name__ == "__main__":
    args = docopt(__doc__, version="1.0")
    main(args)

