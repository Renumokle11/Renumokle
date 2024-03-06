from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/login/')
@app.route('/login/<int:id>')
def check(id =  None):
    if not id:
        message = jsonify(message='id is missing') 
        return make_response(message,  400)
    
    return jsonify(id = id,message = 'you have selected Apples.')


if __name__ == '__main__': 
   
   app.run(debug=True)
          

