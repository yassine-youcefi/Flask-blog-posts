from flask import Flask

application = Flask(__name__)


@application.route('/')
def index(name):
    return "hellow there"


# if __name__ == "__main__":
#     application.run(debug=True, port=5050)
