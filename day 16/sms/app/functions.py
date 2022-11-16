import data

def createStudent(student):
    data.students.append(student)
    print("STUDENT ADDED SUCCESSFULLY")

def getAllStudents():
    print(data.students)
    print("FETCHED ALL STUDENTS")

def getStudentById(id):
    for std in data.students:
        if std['id'] == id:
            print(std)
    print("FETCHED STUDENT BASED ON ID")    
        
        

def updateStudent(id, updatedStudent):
    for std in data.students:
        if std['id'] == id:
            index = data.students.index(std)
            data.students[index] = updatedStudent
            
    print("UPDATED STUDENT DETAILS")

def deleteStudent(id):
    temp = []
    for std in data.students:
        if std['id'] != id:
            temp.append(std)
          
    data.students = temp
