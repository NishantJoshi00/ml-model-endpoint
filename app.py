from flask import Flask, request, url_for, render_template, redirect

from functions import runtimes, get_runtimes

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", functions=runtimes)

@app.route("/model/<int:model_id>", methods=['GET', 'POST'])
def model(model_id):
	if request.method == "GET":
		rt = get_runtimes(model_id)
		if rt == None:
			return redirect("/", code=404)
		return render_template(rt['template'], where="/model/{}".format(model_id))
	else:
		rt = get_runtimes(model_id)
		if rt == None:
			return redirect("/", code=404)
		return rt['model-predict'](request)

if __name__ == "__main__":
	app.run(debug=True)