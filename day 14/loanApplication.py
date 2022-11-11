import random

application = []


def initProcessFunction(type, date):
    formid = random.randint(1000,9999)
    response= {
            "formid" : formid, 
            "req_docs" : ["Doc1", "Doc2"],
            "criteria" : ["Currently studying"],
            "type" : type,
            "date" : date,
            "status" : "pending"
            }
    
    application.append(response)
    return response

def verificationFunction(formid, docs):
    #docs verification
    #update the application status to veirified
    
    for appl in application:
        if appl['formid'] == formid:
            requestedApplication = appl
            requestedApplication['status'] == "verified"
            return requestedApplication
    
    return "Application not found"
     

def approvalFunction():
    return "approved"
    

    
    
    
