from flask import Flask, render_template, request
import sqlite3
from frontend.routes import user_views

application = Flask(__name__)

user_views.index()


if __name__ == '__main__':
    application.run()
