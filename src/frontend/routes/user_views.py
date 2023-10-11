from flask import Flask, render_template, request


@application.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'GET':

    # connection = sqlite3.connect('..backend/database/database.db')
    # cursor = connection.cursor()

    return render_template('index.html')
