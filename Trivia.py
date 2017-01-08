# Author Δημήτρης Φιλίππου

from flask import Flask, render_template, request, redirect, url_for , flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mitsos123@localhost/user_db'
app.config['SECRET_KEY'] = 'super-secret'

app.debug = True

# Create Database
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

    # Query For User
    username = User.query.filter_by(username=request.form['username']).first()
    email = User.query.filter_by(email=request.form['email']).first()


    # Create A Valid User
    if not username and not email:
        user = User(request.form['username'], request.form['email'], 0)
        db.session.add(user)
        db.session.commit()
        return render_template('selector.html', name=request.form['username'], score=user.score , already=False)
    else:
        # Check If User Has Already Played
        if request.form['username'] and request.form['email']:
            # Secure The Login

            user_email_sent = request.form['email']
            server_mail_for_user = User.query.filter_by(username=request.form['username']).first().email

            if user_email_sent  == server_mail_for_user:
                user_score = User.query.filter_by(username=request.form['username']).first().score
                return render_template('selector.html', name=request.form['username'], score=user_score , already=True)
            else:
                flash('Not Authorised!')
                return redirect(url_for('index'))
        else:
            flash("Please Type!")
            return redirect(url_for('index'))


@app.route('/leaderboards')
def leaderboards():
    list = User.query.all()
    return render_template('leaderboards.html', list=list)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/technology')
def tech():
    return render_template('technology.html')


@app.route('/post_ans', methods=['POST'])
def post_ans():
    return redirect(url_for('selector'))


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
