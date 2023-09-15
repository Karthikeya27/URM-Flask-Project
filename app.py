from flask import Flask,render_template,request,jsonify
from database import login_details,register_submitted
app = Flask(__name__)

@app.route("/")
def homepage():
  return render_template("home.html")


@app.route("/loginpage")
def loginpage():
  return render_template("Login.html")

@app.route("/loginsumitted" , methods = ["post"])
def loginsubmitted():
  data = request.form
  login_details(data)
  return jsonify(data)


@app.route("/registration page")
def registerpage():
  return render_template("register.html")

@app.route("/registersubmitted")
def registersubmitted():
  data = request.args
  register_submitted(data)
  return jsonify(data)
  
  
if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug=True)
  