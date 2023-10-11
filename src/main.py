from flask import Flask, render_template, request
import sqlite3

application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'GET':

    # connection = sqlite3.connect('..backend/database/database.db')
    # cursor = connection.cursor()

    return render_template('index.html')


if __name__ == '__main__':
    application.run(debug=False)
