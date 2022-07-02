import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route('/', methods=['GET'])
def home():
    return "<h1>python api test with docker</p>"

app.run()