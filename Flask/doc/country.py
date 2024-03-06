from flask import Flask 
from flask import redirect
from flask import url_for

# instance of flask application
app = Flask(__name__)


@app.route("/India")                #
def Hello_India():
	return "NAMSTE!"




@app.route("/Spain")
def Hello_Spain():
	return "Hola!"



@app.route("/Germany/<capital>")
def Hello_Germany(capital):
	return 'Hola'+ capital +'!'


@app.route("/user/<country>")
def dispaly_user(country):
	if country == 'India':
		return redirect(url_for('Hello_India'))
	elif country == 'Spain':
		return redirect(url_for('Hello_Spain'))
	elif country == 'Germany':
		return redirect(url_for('Hello_Germany', capital ='Frankurt'))



if __name__ == '__main__': 
   app.run(debug=True)
