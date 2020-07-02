"""
This is a Flask app to show the URL Links and the Date the link was posted in the form of a table
"""
#Importing flask module
from flask import Flask
import csv
#Importing render_template to include html files and css.
from flask import render_template

#Give a name to the application, here its 'app'.
app = Flask(__name__)

#Route the application to go to a specific path.
@app.route("/")
def index():
     return render_template("index.html")

@app.route("/read_csv", methods=['GET'])
def read_csv():
    with open ('newsletter_data.csv') as f:
        reader = csv.reader(f, delimiter="\n")
        reader_list=[]
        for row in reader:
            reader_list.append(row[0].split(','))   

    return render_template("index.html", newsletter_data = reader_list)

#'app' is the instance for the Flask application.Run the application in a particular port!!
if __name__=='__main__' :
    app.run(host='0.0.0.0', port=5000, debug= True)