from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/info", methods=["GET"])
def info():
    """
    This endpoint returns information about the model
    """
    return "Model Info"


@app.route("/evaluate", methods=["POST"])
def evaluate():
    """
    This endpoint receives a JSON object of the form:
        {"data": [x0, ..., x783]}
    and returns the predicted number: 0-9
    """
    return str(dir(request))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
