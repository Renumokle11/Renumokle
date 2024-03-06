import flask


from flask import Flask
app = Flask(__name__)

# home route that returns below text when root url is accessed
@app.route("/python/flask")
def print_python():
	return " flask application!"


@app.route('/python/WSGI/')
def print_wsgi():
    return 'WSGI'


if __name__ == '__main__': 
   app.run(debug=True)
