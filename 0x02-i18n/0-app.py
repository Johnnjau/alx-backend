#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    outputs “Welcome to Holberton”
    as a title
    "Hello, world" as a header
    """
    return render_template("0-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
