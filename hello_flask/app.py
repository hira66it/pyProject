from flask import Flask
from datetime import datetime
import re
from flask import render_template
# To run type this "python3 -m flask run" on terminal
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

# @app.route("/")
# def home():
#     return "Hello, Flask!"

# @app.route("/hello/<name>")
# def hello_there(name = None):
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # BAD CODE! Avoid inline HTML for security reason, plus templates automatically escape HTML content.
#     content = "<strong>Hello there, " + name + "!</strong> It's " + formatted_now

#     return render_template(
#         "hello_there.html",
#         name=name,
#         date=datetime.now()
#     )
    
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")