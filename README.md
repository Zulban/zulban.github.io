Meteohack Website
==============

The code in this project generates the static files for `meteohack.ca`.

# Contributing

You can edit the HTML files in `app/templates/en` or `app/templates/fr` like `app/templates/fr/faq.html`.

Then, submit a merge request.

# Setup

Run this script:

```
setup/setup-venv.sh
```

You can now run the test web server. This runs a process so you can view the website in a local web browser at `localhost:5000`:

```
bin/meteohack web
```

You can also build the static files. These are used by `www.meteohack.ca` when uploaded to GitHub for free web hosting:

```
bin/meteohack freeze
```

# Attribution

The Earth logo is free for use with attribution, found [here](https://www.flaticon.com/free-icon/earth_44386).
