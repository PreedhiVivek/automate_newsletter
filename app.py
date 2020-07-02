

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

@app.route("/response", methods=['GET'])
def response():
    with open ('newsletter_data.csv') as f:
        reader = csv.reader(f, delimiter="\n")
        #for i, line in enumerate(reader):
        #    print('line[{}] = {}'.format(i, line))
        print (reader)
    return render_template("index.html", newsletter_data = reader)

#'app' is the instance for the Flask application.Run the application in a particular port!!
if __name__=='__main__' :
    app.run(host='0.0.0.0', port=5000, debug= True)