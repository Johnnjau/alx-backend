#!/usr/bin/en#!/usr/bin/env python3
"""Get locale from request
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """set the default config
    """

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get the local language from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """return Hello, world
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()v python3
"""Get locale from request
"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """set the default config
    """

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get the local language from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """return Hello, world
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
