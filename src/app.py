from flask import Flask, render_template, request
from frontend.routes import user_views

# kjør i terminalen:
# pip install -r requirements.txt
# poetry install
# npm install
# mvn install


application = Flask(__name__)

user_views.display_index()


if __name__ == '__main__':
    application.run(debug=True)
