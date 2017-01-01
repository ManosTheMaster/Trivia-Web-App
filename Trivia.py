from flask import Flask, render_template, request, redirect, url_for , flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mitsos123@localhost/user_db'
app.config['SECRET_KEY'] = 'super-secret'

app.debug = True

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    score = db.Column(db.Integer, unique=False)

    def __init__(self, username, email, score):
        self.username = username
        self.email = email
        self.score = score

    def __repr__(self):
        return '<User %r>' % self.username


# HomePage
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/selector')
def selector(name, score):
    return render_template("selector.html", name=name , score=score)


# Register User
@app.route('/post_user', methods=['POST','GET'])
def post_user():

    username = User.query.filter_by(username=request.form['username']).first()
    email = User.query.filter_by(email=request.form['email']).first()
    if not username and not email:
        user = User(request.form['username'], request.form['email'], 0)
        db.session.add(user)
        db.session.commit()
        return render_template('selector.html', name=request.form['username'], score=user.score)
    else:
        flash("Username Or Email Already Exists",category='message')
        return redirect(url_for('index'))



@app.route('/leaderboards')
def leaderboards():
    list = User.query.all()
    return render_template('leaderboards.html', list=list)


if __name__ == '__main__':
    app.run()
