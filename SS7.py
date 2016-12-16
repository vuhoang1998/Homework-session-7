from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/music")
def music():
    return render_template("Music.html")



if __name__ == '__main__':
    app.run()
