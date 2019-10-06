from flask import Flask ,render_template,request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'newrootpassword'
app.config['MYSQL_DATABASE_DB'] = 'dbms_pro'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method=='POST':
		userDetails=request.form
		name=userDetails['name']
		email=userDetails['email']
		if name=='udhayaakash@gmail.com' and email=='aakash':
			return render_template('user.html')
		else:
			return 'failed'

	elif request.method=='GET':
		return render_template('index.html')

@app.route('/user',methods=['GET','POST'])
def users():
	if request.method=='POST':
		conn = mysql.connect()
		cursor =conn.cursor()
		resultvalue=cursor.execute("SELECT * FROM resource7")
		print('hi dude')
		if resultvalue > 0:
			userDetails=cursor.fetchall();
			print (userDetails)
		return render_template('resource table.html',userDetails=userDetails)
	elif request.method=='GET':
	 	return render_template('user.html')

@app.route('/details',methods=['GET','POST'])
def details():
	print('hi')
	if request.method=='POST':
		conn = mysql.connect()
		cursor =conn.cursor()
		resultvalue=cursor.execute("SELECT * FROM resource1")
		print('hi dude')
		if resultvalue > 0:
			userDetails=cursor.fetchall();
			print (userDetails)

	elif request.method=='GET':
		conn = mysql.connect()
		cursor =conn.cursor()
		resultvalue=cursor.execute("SELECT * FROM employee")
		print('hi dude')
		if resultvalue > 0:
			userDetails=cursor.fetchall();
			print (userDetails)
		return render_template('employee table.html',userDetails=userDetails)

@app.route('/proj',methods=['GET','POST'])
def uusers():
	if request.method=='POST':
		conn = mysql.connect()
		cursor =conn.cursor()
		resultvalue=cursor.execute("SELECT * FROM project1")
		print('hi dude')
		if resultvalue > 0:
			userDetails=cursor.fetchall();
			print (userDetails)
		return render_template('proj.html',userDetails=userDetails)
	elif request.method=='GET':
		conn = mysql.connect()
		cursor =conn.cursor()
		resultvalue=cursor.execute("SELECT * FROM project7")
		print('hi dude')
		if resultvalue > 0:
			userDetails=cursor.fetchall();
			print (userDetails)
		return render_template('project.html',userDetails=userDetails)


if __name__ == '__main__':
	app.run(debug=True) 