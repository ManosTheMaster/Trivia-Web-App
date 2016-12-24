from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for

score = 0

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mitsos123@localhost/flaskmovies'
app.debug = False
# db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __repr__(self):
#         return '<User %r>' % self.username


@app.route('/')
def index():
    score = 0
    return render_template("index.html")

@app.route('/technology')
def technology():
    return render_template("technology.html")



# @app.route('/')
# def index():
#     myUser = User.query.all()
#     oneItem = User.query.filter_by(username="jimfilippou").first()
#     return render_template("start.html", myUser=myUser , admin=oneItem)


# @app.route('/profile/<identity>')
# def profile(identity):
#     user = User.query.filter_by(username=identity).first()
#     return render_template("profile.html", user=user)


# @app.route('/post_user', methods=['POST'])
# def post_user():
#     user = User(request.form['username'], request.form['email'])
#     db.session.add(user)
#     db.session.commit()
#     return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
