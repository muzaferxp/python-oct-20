from flask import Flask, render_template, request
from readData import getData
from datetime import datetime
import json

app = Flask(__name__)


@app.route("/")
def index():
    data = getData()
    return render_template("index.html", blogs = data['blogs'])



@app.route("/create-blog", methods=['GET','POST'])
def create_blog():
    if request.method == "POST" :
        #read the user input of new blog
        
        blog = {
            "title": request.form['title'],
           "description": request.form['desc'], 
        "tag": request.form['tag'],
        "posted_on": str(datetime.now())
        }
        
        data = getData()

        #save the new blog to json file
        f = open("blogs.json", "w")
        
        data['blogs'].append(blog)
        
        f.write(json.dumps(data))
        
        f.close()

        
        
        
    return render_template("create-blog.html")



if __name__ == "__main__":
    app.run()





























