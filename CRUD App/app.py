from flask import Flask, render_template, url_for,redirect, request, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Haripriya@2002"
app.config["MYSQL_DB"] = "student"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql=MySQL(app)


@app.route("/")
def home():
    con=mysql.connection.cursor()
    sql="SELECT*FROM students"
    con.execute(sql)
    res=con.fetchall()
    return render_template("home.html", datas=res)



@app.route("/addUsers", methods=['GET','POST'])
def addUsers():
    if request.method == 'POST':
        id=request.form['id']
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        flash('User Details Added')
        con=mysql.connection.cursor()
        sql="INSERT INTO students(id,name,email, phone) value (%s,%s,%s,%s)"
        con.execute(sql,[id,name, email,phone])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    return render_template("addUsers.html")



@app.route("/editUser/<string:id>", methods=['GET','POST'])
def editUser(id):
    con=mysql.connection.cursor()
    if request.method == 'POST':
        # id=request.form['id']
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        
        sql="UPDATE students SET name=%s, email=%s, phone=%s WHERE id=%s"
        con.execute(sql,[name, email,phone,id])
        mysql.connection.commit()
        con.close()
        flash('User Details Updates')
        return redirect(url_for("home"))
    
    sql="select*from students where ID=%s"
    con.execute(sql,[id])
    res=con.fetchone()
    return render_template("editUser.html", datas=res)



@app.route("/deleteUser/<string:id>",methods=['GET','POST'])
def deleteUser(id):
    con=mysql.connection.cursor()
    sql="DELETE FROM students WHERE id=%s"
    con.execute(sql,[id])
    mysql.connection.commit()
    con.close()
    flash('User Details Deleted')
    return redirect(url_for("home"))



if(__name__ == '__main__'):
    app.secret_key="abc123"
    app.run(debug=True)
    
