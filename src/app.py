from flask import Flask, render_template, url_for

# definerer hvor templates ligger
application = Flask(__name__, template_folder='frontend/templates')


# våre paths:
@application.route('/')
def index():

    return render_template('/index.html')


@application.route('/registrer')
def registrer_page():

    return render_template('/registrer.html')


@application.route('/homepage')
def homepage():

    return render_template('/homepage.html')


if __name__ == '__main__':
    application.run(debug=True)
