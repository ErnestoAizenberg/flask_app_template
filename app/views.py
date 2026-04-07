"""Views"""

from flask import render_template

def read_root():
    return render_template('index.html')