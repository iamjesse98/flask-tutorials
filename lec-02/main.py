from flask import Flask

app = Flask(__name__)

#index page
@app.route('/')
def index():
	return 'Hello from homepage'

#localhost:5000/jesse
@app.route('/jesse')  
def jesse():
	return 'Hello from jesse page'
	
app.run()