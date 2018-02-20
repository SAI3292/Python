from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
	return "my page is done"

@app.route('/about/')
def template():
	return render_template("home.html")


if __name__ =="__main__":
	app.run(debug=True)
