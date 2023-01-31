#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)

babel = Babel(app)

class Config(object):
    """configure Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
"""Use class config for your Flask app."""


@app.route("/")
def home():
    """basic flask app"""
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    locl = request.args.get("locale");
    approvedLocal = app.config["LANGUAGES"]
    if locl in approvedLocal:
        return locl
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
