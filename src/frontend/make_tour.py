from flask import Flask, render_template, url_for
import sqlite3


app = Flask(__name__)


def get_db_connetion():
    conn = sqlite3.connect('../backend/database/database.db')
    conn.row_factory = sqlite3.Row
    return conn



# Root page
@app.route("/")
def root():
    conn = get_db_connetion()


    return render_template('make_tour_index.html')


if __name__ == "__main__":
    app.run(debug=True)