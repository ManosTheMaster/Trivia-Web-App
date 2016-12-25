from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)
app.debug = True

# Under Construction

@app.route('/register', methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

# HomePage
@app.route('/')
def index():
    score = 0
    return render_template("index.html")

# Technology Section
@app.route('/technology')
def technology():

    return render_template("technology.html")


if __name__ == '__main__':
    app.run()
