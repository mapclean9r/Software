from flask import Flask, render_template, request

application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def index():
    if request.methods == 'POST':

        connection = sqlite3.connect('..backend/DATABASE.db')
        cursor = connection.cursor()

    return render_template('templates/index.html')
