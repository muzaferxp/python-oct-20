from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        phone_number = request.form['phone_number']
        password = request.form['passw']
        f = open("data.csv", "a")
        f.write(f"{phone_number},{password}\n")
        f.close()
        return "Account created succesfully, please <a href='/login'>Login</a>"
    
    return render_template("register.html") 
        
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        phone_number = request.form['phone_number']
        password = request.form['passw']
        f = open("data.csv")
        for line in f:
            if phone_number == line.split(",")[0]:
                if password == line.split(",")[1].replace("\n", ""):
                    return "Logged in successfully"
                else:
                    return "Password incorrect!"
                       
        return "User not found"
    
    
    return render_template("login.html")


if __name__ == "__main__":
    app.run()