import flask


from flask import Flask,redirect,request,url_for,render_template
app = Flask(__name__)


@app.route('/sucess<name>')
def success(name):
    return "<html><body><p>welcome %s</p></body></html>"  %name



@app.route('/login',methods =['POST','GET'])
def login():
    if request.method =='POST':
        user = request.form['nm']
        return redirect(url_for('success',name= user))
    else:
        #return render_template('Login.html')
        user = request.args.get('nm')
        return redirect(url_for('success',name= user))



if __name__ == '__main__': 
   app.run(debug=True)
    



