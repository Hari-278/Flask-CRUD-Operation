from flask import Flask, render_template, request, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Haripriya@2002'
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT*FROM students")
    data = cur.fetchall()
    cur.close()
    
    return render_template('index.html', students=data)
    
    
if __name__ == "__main__":
    app.run(debug=False)