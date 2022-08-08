from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='python'

mysql=MySQL(app)

@app.route('/',methods=['POST','GET'])
def myhome():
    if request.method=='POST':
        fm=request.form
        a=fm['ename']
        b=fm['econtact']
        c=fm['eemail']
        d=fm['esalary']
        cursor=mysql.connection.cursor()
        q="insert into emp(name,contact,email,salary) values('"+a+"','"+b+"','"+c+"','"+d+"')"
        cursor.execute(q)
        mysql.connection.commit()
        print('save success')
        return redirect('/')
    else:
        return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/show')
def show():
    cursor=mysql.connection.cursor()
    q="select * from emp"
    res=cursor.execute(q)
    if(res>0):
        det=cursor.fetchall()
        return render_template('show.html',details=det)
    else:
        return render_template('show.html')

@app.route('/update/<string:id>')
def update(id):
    cursor=mysql.connection.cursor()
    q="select * from emp where id='"+id+"'"
    res=cursor.execute(q)
    if(res>0):
        det=cursor.fetchall()
        return render_template('update.html',details=det)

@app.route('/edit',methods=['POST','GET'])
def edit():
    if request.method=='POST':
        fm=request.form
        a=fm['ename']
        b=fm['econtact']
        c=fm['eemail']
        d=fm['esalary']
        e=fm['oid']
        cursor=mysql.connection.cursor()
        q="update emp set name='"+a+"',contact='"+b+"',email='"+c+"',salary='"+d+"' where id='"+e+"'"
        cursor.execute(q)
        mysql.connection.commit()
        return redirect('/show')

@app.route('/delete/<string:id>')
def delete(id):
    cursor=mysql.connection.cursor()
    q="delete from emp where id='"+id+"'"
    cursor.execute(q)
    mysql.connection.commit()
    return redirect('/show')

app.run(debug=True)