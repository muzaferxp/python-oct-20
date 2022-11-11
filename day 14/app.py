from flask import *
import loanApplication

app = Flask(__name__)


@app.route("/")
def index():
    return "welcome"



@app.route("/initiate-process")
def initiateProcess():
    
    Type = request.args.get("type")
    Date = request.args.get("date")
    
    res = loanApplication.initProcessFunction(Type, Date)
    return {"data" : res, }


@app.route("/verification")
def verification():
    formid = request.args.get("formid")
    res = loanApplication.verificationFunction(int(formid), [])
    return {"data" : res}

@app.route("/approve")
def approve():
    return "welcome"


@app.route("/get-all-application")
def getAllApplications():
    return {"data" :  loanApplication.application}


if __name__ == "__main__":
    app.run()