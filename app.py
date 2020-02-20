from flask import Flask , render_template , request

app = Flask(__name__)


@app.route('/')

def index():

	return render_template('index.html')


@app.route('/home')

def home():

	results = { "physics" : 70 , "Math" : 60 , "English" : 80 }

	return render_template('home.html' , result = results )

@app.route('/register')

def register():

	return render_template('register.html' , error = None)


@app.route('/login')

def login():

	return render_template('login.html' , error = None)

@app.route('/checkUser' , methods=['POST'])

def check_user():

	data = request.form

	if data['uu'] == 'abc' and data['password'] == '12345678' :

		return render_template('home.html')

	else:

		return render_template('login.html' , error = "invalid credentials")




@app.route('/addUser' , methods=['POST'])

def add_user():

	data = request.form

	if data['contact'] == '':

		return render_template('register.html' , error = "Check Contact number")

	else:
		return "Registered successfully";


if __name__=="__main__":

	app.run()
