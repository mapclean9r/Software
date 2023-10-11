from flask import Flask


app = Flask(__name__)


# Root page
@app.route("/")
def root():
    return "You are on the root landing site"


if __name__ == "__main__":
    app.run(debug=True)