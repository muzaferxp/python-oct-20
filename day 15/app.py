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
    
    if Type == None:
        return {"sucess" : False, "message" : "Loan type is required"}
    
    if Date == None:
        return {"sucess" : False, "message" : "Date is required"}
    
    
    res = loanApplication.initProcessFunction(Type, Date)
    return {"data" : res, "message" : "Application added successfully" , "sucess" : True }


@app.route("/verification")
def verification():
    formid = request.args.get("formid")
    res = loanApplication.verificationFunction(int(formid), [])
    return {"data" : res}

@app.route("/approve")
def approve():
    #access user send inpur
    formid = request.args.get("formid")
    
    #calling the approvalFunction
    res = loanApplication.approvalFunction(int(formid))
    
    return {"data" : res}


@app.route("/get-all-application")
def getAllApplications():
    return {"data" :  loanApplication.application}


if __name__ == "__main__":
    app.run(debug=True)