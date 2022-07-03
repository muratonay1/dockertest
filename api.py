from flask import Flask
from Controller import *
from Constant import *
app = Flask(__name__)

@app.route('/')
def hello_world():
	return pullUserCollection(DB_PATH_RECORDS)

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)