from flask import Flask, request


app = Flask(__name__)


@app.after_request
def after(response):
    if request.method == "GET":
        response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/weeby/magic")
def hello_world():
    # Happy hacking :)
    return "hello, world"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337)
