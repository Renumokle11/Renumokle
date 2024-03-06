import flask


from flask import Flask,redirect,request,url_for,render_template
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route('/upload')
def upload_view():
    return  render_template('upload.html')



@app.route('/uploader', methods =['GET','POST'])
def uploading():
    if request.method =='POST':
        file = request.files['file']
        file.save(secure_filename(file.filename))
        return "file uploaded successfully"




if __name__ == '__main__': 
   app.run(debug=True)
    