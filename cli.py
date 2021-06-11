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

def main(args):
        
    if args["web"]:
        app=create_app()
        
        app.run(host=args["--host"],
                port=int(args["--port"]),
                threaded=True)        
    
    elif args["freeze"]:
        raise NotImplemented
    
    print("Done.")

if __name__ == "__main__":
    args = docopt(__doc__, version="1.0")
    main(args)

