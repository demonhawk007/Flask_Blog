from flask import Flask, render_template, url_for
app = Flask(__name__)

Posts = [
    {
        'author':'Shishir',
        'title':'Blog 1',
        'content':'Once upon a time',
        'date_posted':'18th Sept, 2019'
    },
    {
        'author':'John',
        'title':'Blog 2',
        'content':'There lived a person',
        'date_posted':'19th Sept, 2019'
    }
]

@app.route("/")
@app.route("/Home")
def Home():
    return render_template('home.html',posts=Posts)


@app.route("/About")
def About():
    return render_template('about.html', title="About")


if __name__ == '__main__':
    app.run(debug=True)