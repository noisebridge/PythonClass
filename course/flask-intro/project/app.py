from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/blog/")
def blog():
    return render_template("blog.html")

if __name__ == "__main__":
    app.run()
