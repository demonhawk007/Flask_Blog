from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b18c1bffe490ac2a15d21e5555537eab'

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

@app.route("/Register",methods=['GET','POST'])
def Register():
    form = RegistrationForm()
    return render_template('register.html',title='Register',form = form)

@app.route("/Login", methods=['GET','POST '])
def Login():
    form = LoginForm()
    return render_template('login.html',title='Login',form = form)

if __name__ == '__main__':
    app.run(debug=True)