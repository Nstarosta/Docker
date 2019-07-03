from flask import Flask , render_template
from mysqldb import mysqldb

db = MySQLdb.connect("localhost","dockerimg")

app= Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')
if __name__ == '__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)