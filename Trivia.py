from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)
app.debug = True


# HomePage
@app.route('/')
def index():
    score = 0
    return render_template("index.html")

# Technology Section
@app.route('/technology')
def technology():
    return render_template("technology.html")


# Register User
@app.route('/post_user', methods=['POST'])
def post_user():
    return 1

if __name__ == '__main__':
    app.run()
