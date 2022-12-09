from flask import *
import core
app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to Fliplart api v1.0"

@app.route("/search")
def search():
    search_query = request.args.get("product_name")
    data =  core.searchProduct(search_query)
    return {
        "You have searched for" : search_query, 
        "No.of records fetched" : len(data),
        "data" : data
    }
    

if __name__=="__main__":
    app.run(debug=True)