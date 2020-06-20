from flask import Flask, request, url_for, render_template

from functions import runtimes

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", functions=runtimes)

@app.route("/model/<int:model_id>", methods=['GET', 'POST'])
def model(model_id):
	pass

if __name__ == "__main__":
	app.run(debug=True)