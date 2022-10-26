from flask import Flask
from flask_cors import CORS, cross_origin #cross origin access


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


data = {
    "user1" : ["Name 1", "Number 1", "Email 1"],
    "user2" : ["Name 2", "Number 2", "Email 2"],
    "user3" : ["Name 3", "Number 3", "Email 3"],
}



@app.route("/")
def home():
    return "Home page"

@app.route("/profile/<id>")
def profile(id):
    return {"profile_details" : data[id]}


@app.route("/about")
def about():
    return "About page"

@app.route("/services")
def services():
    return "Services"



if __name__ == "__main__":
    app.run()

