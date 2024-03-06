

from flask import Flask

# instance of flask application
app = Flask(__name__)

# home route that returns below text when root url is accessed
@app.route("/")
def hello_world():
	return "<p>Hello</p>"


@app.route('/user/<string:name>')
def greeting(name):
      return 'Hi' + name

@app.route('/uniqueid/<uuid:api_key>')
def display_key(api_key):
      return "THE API KEY" + str(api_key)

@app.route('/path/<path:sub_path>')
def display_path(sub_path):
      return sub_path

app.add_url_rule('/hello','hello', hello_world)

if __name__ == '__main__': 
   app.run(debug=True)
