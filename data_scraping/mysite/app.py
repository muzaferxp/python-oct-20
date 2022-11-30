from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    
    f = open("mysite/data/data.csv")
    data = []
    for line in f:
        data.append(line.split(","))
    f.close()
    return render_template("index.html", data = data, c_count = len(data))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000, debug=True)