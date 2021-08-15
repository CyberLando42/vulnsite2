from flask import Flask, url_for, render_template, abort, send_file, request, redirect, session

app = Flask(__name__)
app.secret_key = "237489237489234782394723894"

@app.route('/')
def index():
    session["admin"] = "false"
    return render_template("index.html")
    

@app.route('/static/secret.txt')
def ssrf():
	abort(403)



@app.route("/image")
def image():
	image_file = request.args.get('image', '')
	return send_file(f"{image_file}")
  
@app.route("/admin")
def admin():
	if session["admin"]:
		if session["admin"] == "true":
			return render_template("admin.html")
		else:
			abort(403)
	else:
		return(redirect(url_for("index")))
		

app.run()
