from Trivia import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    score = db.Column(db.Integer, unique=False)
    technology = db.Column(db.Boolean)
    history = db.Column(db.Boolean)
    sports = db.Column(db.Boolean)

    def __init__(self, username, email, score):
        self.username = username
        self.email = email
        self.score = score
        self.technology = False
        self.sports = False
        self.history = False

    def __repr__(self):
        return '<User %r>' % self.username