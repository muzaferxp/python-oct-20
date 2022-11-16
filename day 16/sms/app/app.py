import data
import functions

student = {
    "id" : "8",
    "name" : "Fahad",
    "phone" : "+91987654321",
    "class" : "class 8"
}

functions.createStudent(student)
functions.getAllStudents()
functions.getStudentById("6")
functions.updateStudent("8", {
                                    "id" : "8",
                                    "name" : "Fahad Khan",
                                    "phone" : "+91987654321",
                                    "class" : "class 8"
                            })
functions.getAllStudents()
functions.deleteStudent("6")
functions.getAllStudents()