from flask import Flask

app = Flask(__name__)


@app.route("/")
def Hello():
    return "Hello World"


@app.route("/second")
def second():
    return "This is the second page"


@app.route("/third/subthird")
def third():
    return "This is subpage of the third page"


@app.route("/forth/<string:id>")
def fourth(id):
    return f"The id of this page is {id}"


if __name__ == "__main__":
    app.run(debug=True)
