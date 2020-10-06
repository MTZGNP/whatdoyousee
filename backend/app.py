from flask import Flask , session , request
from MySQLdb import _mysql as sql
db=sql.connect(host="whatdoyousee.mysql.pythonanywhere-services.com",user="whatdoyousee",passwd="bigmoonshower",db="whatdoyousee$test")


frontend_url = ""
app = Flask(__name__)
app.secret_key = ''
@app.route("/api/register" , methods = ["POST"])
def register():
    if 'registered' in session:
        return "wot"
    else:
        session['registered'] = True
        session['id'] = None
if __name__ == "__main  __":
    pass
