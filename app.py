from flask import Flask, render_template, url_for


application = Flask(__name__)

posts = [

    {
        'author': 'yassine youcefi',
        'title': 'Blog jdid hada 1',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 21'
    },
    {
        'author': 'chaindraa wahid',
        'title': 'Blog jdid hada 2',
        'content': 'my first blog for test it is hardcoded',
        'date_posted': 'April 22'

    }
]


@application.route('/')
@application.route('/home')
def home():
    return render_template('index.html', posts=posts)


@application.route('/about')
def about():
    return render_template('about.html', title='About')

# if __name__ == "__main__":
#     application.run(debug=True, port=5050)
