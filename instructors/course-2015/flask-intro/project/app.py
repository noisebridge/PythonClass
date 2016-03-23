from flask import Flask, render_template, send_from_directory


app = Flask(__name__)

@app.route("/assets/<path:path>")
def send_assets(path):
    return send_from_directory('assets', path)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/blog/")
def blog():
    return render_template("blog.html")

if __name__ == "__main__":
    app.run()
