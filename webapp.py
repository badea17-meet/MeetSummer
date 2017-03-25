from flask import Flask, url_for, flash, redirect, request, render_template, send_from_directory
from flask import session as login_session
from werkzeug.utils import secure_filename
import locale, os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Home.html")


if __name__ == '__main__':
	app.run(debug=True)