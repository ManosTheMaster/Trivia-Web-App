
from flask import Flask, render_template, request, redirect, url_for , flash
from flask_sqlalchemy import SQLAlchemy
import yaml

with open("C:/Users/FrozenVortex/Documents/Blackpeak/Trivia-Web-App/settings.yml", 'r') as stream:
    data = yaml.safe_load(stream)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = data['servers']['digital_ocean']['postgres']
app.config['SECRET_KEY'] = data['servers']['digital_ocean']['key']

app.debug = True

# Create Database
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    score = db.Column(db.Integer, unique=False)
    technology = db.Column(db.Boolean, unique=False)

    def __init__(self, username, email, score):
        self.username = username
        self.email = email
        self.score = score
        self.technology = False

    def __repr__(self):
        return '<User %r>' % self.username


# HomePage
@app.route('/')
def index():
    return render_template("index.html")

# User Selects Category Here
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
            flash("Please Type Something!")
            return redirect(url_for('index'))


# Classic Leaderboards
@app.route('/leaderboards')
def leaderboards():
    list = User.query.all()
    return render_template('leaderboards.html', list=list)

# Information ABout Game
@app.route('/about')
def about():
    return render_template('about.html')

# Technlogy questions
@app.route('/technology/<string:who>')
def tech(who):
    return render_template('technology.html', user=who)


@app.route('/post_tec/<string:name>', methods=['POST'])
def post_tec(name):
    if request.method == 'POST':
        pts = 0
        points = []
        for k in range(10):
            points.append(request.form["q%s" % str(k)])

        for index, item in enumerate(data['answers']['technology']):
            if points[index] == item:
                pts += 1

        # Change The Score Of That User
        current = User.query.filter_by(username=name).first()
        current.score += pts

        # Change Technology Boolean
        current.technology = True

        # Commit Changes
        db.session.commit()

        return "You Won %s Points You Piece Of Shit! <br> This Page Looks Ugly And It Is Until A Front-End Fixes This Shit. <br> Anyway Here is What Changed <br> <ul><li>You Got %s Points</li><li>You Can't Play Anymore This Section Cause You Already Know The Answers</li><li>You Gave Satisfaction To The Developer Who Spent All This Time For Your Interaction With This Web App</li></ul>" %(str(pts),str(pts))

if __name__ == '__main__':
    app.run()
