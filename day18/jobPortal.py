import data

def searchJob(title):
    for job in data.JOB_PORTAL_DATA:
        if job['Title'] == title:
            print(job)
            
def jobApplication(jobId):
    for job in data.JOB_PORTAL_DATA:
        if job['id'] == jobId:
            data.MY_APPLICATIONS.append(job)
    
def myApplication():
    print(data.MY_APPLICATIONS)
    
def getAllJobs():
    print(data.JOB_PORTAL_DATA)
    

def updateApplicationStatus(id, status):
    for application in data.MY_APPLICATIONS:
        if application['id'] == id:
            index = data.MY_APPLICATIONS.index(application)
            
            updateApplication = application
            updateApplication['status'] = status
            data.MY_APPLICATIONS[index] = updateApplication
            
            