from flask import Flask, render_template
import getData

app = Flask(__name__)

@app.route("/home/<char>")
def home(char):
    
    #getting data from the csv file 
    data = getData.getDataByChar(char)
    
    options = getData.getOptions()
    
    return render_template("home.html", charValue = data, options = options)


if __name__ == "__main__":
    app.run()


