from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from mysql import connector
import re
from datetime import datetime


app = Flask(__name__)                                    #(static_folder="./Login/static")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.secret_key = 'abc_2345/aspqr/'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config["MYSQL_PORT"] = '3306'
app.config['MYSQL_PASSWORD'] = 'Renu1115'
app.config['MYSQL_DB'] = 'geeklogin'



#mysql = MySQLdb.connect("localhost", "root", "Renu1115", "geeklogin")
mysql = MySQL(app)
mysql.init_app(app)

def get_connection():
    conn = connector.connect(host= "localhost",user="root",password="Renu1115",port=3306,database="geeklogin")
    return conn

@app.route("/")
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()

        if not username or not password:
            msg = 'Please fill out all the required fields!'
        elif ' ' in username or ' ' in password:
            msg = 'Username and password should not contain spaces!'
        if not username:
            msg['username'] = 'Please enter a username!'
        if username and not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$', username):
            msg['username'] = 'username must contain characters,numbers, and one special character!'
        elif not password or not re.match(r'^[A-Za-z0-9!@#$%^&*()_+=\-{}\[\]:;"\'|\\<,>.?\/]+$', password):
            msg = 'Invalid password! Password must contain characters, numbers, and special characters.'

        if msg:
            return render_template('login.html', msg=msg)

        session['username'] = username
        session['password'] = password

        
        conn = get_connection()
        cursor = conn.cursor()
        query = f'SELECT * FROM personal_details WHERE username = "{session["username"]}" and password = "{session["password"]}";'
        cursor.execute(query)
        user_details = cursor.fetchone()

        db_columns = ["id", "username", "password", "email", "phonenumber", "Name", "aadharcard_number", "pancard_number", "emp_id", "emp_name", "company_name", "designation", "date_of_joining", "street", "society", "landmark", "city", "state", "pincode"]

        if user_details:
            user_details = dict(zip(db_columns, user_details))
            for det in user_details:
                session[det] = user_details[det]
            session['loggedin'] = True

            if 'aadharcard_number' not in user_details or 'pancard_number' not in user_details:
                return redirect(url_for('kyc_details'))
            elif 'emp_id' not in user_details or 'emp_name' not in user_details or 'company_name' not in user_details or 'designation' not in user_details or 'date_of_joining' not in user_details:
                return redirect(url_for('employee_details'))
            elif 'street' not in user_details or 'society' not in user_details or 'landmark' not in user_details or 'city' not in user_details or 'state' not in user_details or 'pincode' not in user_details:
                return redirect(url_for('address_details'))
            else:
                return redirect(url_for('profile', msg='Logged in successfully!'))
        else:
            msg = 'Incorrect username or password!'
    return render_template('login.html', msg=msg)

           
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))
                                                    

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg=''
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()
        email = request.form.get('email', '').strip()
        phonenumber = request.form.get('phonenumber', '').strip()
        name = request.form.get('Name', '').strip()

        session['username'] = username

        # Validate fields
        msg = {}

        if not username:
            msg['username'] = 'Please enter a username!'
        if username and not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$', username):
            msg['username'] = 'username must contain characters,numbers, and one special character!'
        if not password:
            msg['password'] = 'Please enter a password!'
        if password and not re.match(r'^[A-Za-z0-9!@#$%^&*()_+=\-{}\[\]:;"\'|\\<,>.?\/]+$', password):
            msg['password'] = 'Password must contain at least one special character!'
        if password != confirm_password:
            msg['confirm_password'] = 'Passwords do not match!'

        if not email: 
            msg['email'] = 'Please enter a email!'
        if email  and  not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg['email'] = 'Invalid email address!'
        if not phonenumber or not phonenumber.isdigit():
            msg['phonenumber'] = 'Phone number must contain only digits and not start with 1,2,3!'
        if not name or len(name) < 3:
            msg['name'] = 'Full Name should contain at least 3 characters!'

        if msg:
            return render_template('register.html',msg=msg)

        conn = get_connection()
        cursor = conn.cursor()
        query = f'INSERT INTO personal_details (username, password, email, phonenumber, Name) VALUES ("{username}", "{password}", "{email}", "{phonenumber}", "{name}");'
        cursor.execute(query)
        conn.commit()
        return redirect(url_for('kyc_details'))

    return render_template('register.html',msg=msg)

@app.route('/kyc_details', methods=['GET', 'POST'])
def kyc_details():
    msg = ''
    if request.method == 'POST':
        aadharcard_number = request.form.get('aadharcard_number').strip()
        pancard_number = request.form.get('pancard_number').strip()

        

        if not aadharcard_number or not pancard_number:
            msg = 'Please fill out all the required fields!'
        
        elif not re.match(r'^\d{4}\s\d{4}\s\d{4}$',aadharcard_number):
            msg= " Please enter in XXXX XXXX XXXX format and Aadhar number must contain only digits"

        
        elif not re.match(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', pancard_number):
            msg = "Invalid PAN card number format. Please enter in ABCDE1234F format."

        if msg:
            return render_template('kyc_details.html', msg=msg)

        
        session['aadharcard_number'] = aadharcard_number
        session['pancard_number'] = pancard_number

        
        query = f'SELECT id FROM personal_details WHERE username = "{session["username"]}";'
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        user_details = cursor.fetchone()
        
        conn = get_connection()
        cursor = conn.cursor()
        query_check = f'SELECT user_id FROM kyc_details WHERE  aadharcard_number = "{session['aadharcard_number']}" AND pancard_number = "{session['pancard_number']}";'
        cursor.execute(query_check)
        existing_kyc = cursor.fetchone()
        if existing_kyc:
            msg = 'Duplicate entry! KYC details already exist in the database.'
            return render_template('kyc_details.html', msg=msg)   
           
        conn = get_connection()
        cursor = conn.cursor()
        query = f'INSERT INTO kyc_details (user_id, aadharcard_number, pancard_number) VALUES ("{int(user_details[0])}","{aadharcard_number}","{pancard_number}");'
        cursor.execute(query)
        conn.commit()
        msg = 'You have successfully submitted!'
        return redirect(url_for('employee_details'))

    return render_template('kyc_details.html', msg=msg)

@app.route('/employee_details', methods=['GET', 'POST'])
def employee_details():
    msg=''
    
    if request.method == 'POST':
        emp_id = request.form.get('emp_id')
        emp_name = request.form.get('emp_name')
        company_name = request.form.get('company_name')
        designation = request.form.get('designation')
        date_of_joining_str = request.form.get('date_of_joining')
       

        if not emp_id or not emp_name or not company_name or not designation :
            error_msg = 'Please fill out all the required fields!'
            return render_template('employee_details.html', error=error_msg)
    
           
        elif not emp_id.strip() or not emp_id.isdigit():
            error_msg = 'Invalid employee ID. Please enter a valid numeric ID.'
            return render_template('employee_details.html', error=error_msg)
        
      
        elif not emp_name.strip():
            error_msg = 'Invalid employee name. Please enter a valid name.'
            return render_template('employee_details.html', error=error_msg)
        
        
        elif not company_name.strip():
            error_msg = 'Invalid company name. Please enter a valid name.'
            return render_template('employee_details.html', error=error_msg)
    
        
        elif not designation or not designation.strip():
            error_msg = 'Invalid designation. Please enter a valid designation.'
            return render_template('employee_details.html', error=error_msg)

        
        elif not date_of_joining_str:
            error_msg = 'Invalid date of joining. Please enter a date.'
            return render_template('employee_details.html', error=error_msg)
        try:
            date_of_joining = datetime.strptime(date_of_joining_str, "%Y/%m/%d").date()
        except ValueError:
            error_msg = 'Invalid date format. Please enter the date in YYYY/MM/DD format.'
            if msg:
                return render_template('employee_details.html', error=error_msg)
        
        session['emp_id'] = emp_id
        session['emp_name'] = emp_name
        session['company_name'] = company_name
        session['designation'] = designation
        session['date_of_joining'] = date_of_joining
    
        conn = get_connection()
        cursor = conn.cursor()
        
        query = f'''UPDATE personal_details SET emp_id="{emp_id}", emp_name="{emp_name}",company_name="{company_name}",designation="{designation}",date_of_joining="{date_of_joining}" WHERE username="{session['username']}"'''
        cursor.execute(query)
        conn.commit()
        conn.close()
        msg = 'You have successfully submitted!'
        return redirect(url_for('address_details'))
    return render_template('employee_details.html')


@app.route('/address_details', methods=['GET', 'POST'])
def address_details():
    msg=''
    if request.method == 'POST':
        street = request.form.get('street')
        society = request.form.get('society')
        landmark = request.form.get('landmark')
        city = request.form.get('city')
        state = request.form.get('state')
        pincode = request.form.get('pincode')

        if not street or not society or not landmark or not city or not state or not pincode:
           error_msg = 'Please fill out all the required fields!'
           return render_template('address_details.html', error=error_msg)

        elif  not street.strip():
            error_msg = 'Invalid street address. Please enter a valid address.'
            return render_template('address_details.html', error=error_msg)

        
        elif not society.strip():
            error_msg = 'Invalid society name. Please enter a valid name.'
            return render_template('address_details.html', error=error_msg)
    
        elif  not landmark.strip():
            error_msg = 'Invalid landmark. Please enter a valid landmark.'
            return render_template('address_details.html', error=error_msg)
        
       
        elif not city.strip():
            error_msg = 'Invalid city name. Please enter a valid name.'
            return render_template('address_details.html', error=error_msg)
        
        elif  not state.strip():
            error_msg = 'Invalid state name. Please enter a valid name.'
            return render_template('address_details.html', error=error_msg)
        
       
        elif not pincode.strip() or not re.match(r'^\d{6}$', pincode):
            error_msg = 'Invalid pincode. Please enter a valid 6-digit pincode.'
            return render_template('address_details.html', error=error_msg)
        
        session['street'] = street
        session['society'] = society
        session['landmark'] = landmark
        session['city'] = city
        session['state'] = state
        session['pincode'] = pincode

        
        query = f'''UPDATE personal_details SET street="{street}", society="{society}",landmark="{landmark}",city="{city}",state="{state}",pincode="{pincode}" WHERE username="{session['username']}" '''
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        msg = 'You have successfully submitted!'
        print(msg)
        return redirect(url_for('profile'))
    return render_template('address_details.html',msg=msg)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'loggedin' in session:
        username = session.get('username')
        password = session.get('password')
        email = session.get('email')
        phonenumber = session.get('phonenumber')
        Name=session.get('Name')
        street = session.get('street')
        society = session.get('society')
        landmark =session.get ('landmark')
        city=session.get ('city')
        state= session.get('state')
        pincode=session.get('pincode')
        emp_id = session.get('emp_id')
        emp_name = session.get('emp_name')
        company_name = session.get('company_name')
        designation = session.get('desiganation')
        date_of_joining = session.get('date_of_joining')
        aadharcard_number = session.get('aadharcard_number')
        pancard_number= session.get('pancard_number')
        
        conn = get_connection()
        cursor = conn.cursor()
        # Query to retrieve data from personal_details and kyc_details tables
        query = f''' SELECT pd.username,pd.password,pd.email,pd.phonenumber,pd.street,pd.society,pd.landmark,pd.city,pd.state,pd.pincode,pd.name,pd.emp_id,
        pd.emp_name,pd.company_name,pd.designation,pd.date_of_joining,pd.Name, kd.aadharcard_number, kd.pancard_number FROM personal_details pd
        INNER JOIN kyc_details kd ON pd.id = kd.user_id
        WHERE pd.username = "{username}"'''
    
        cursor.execute(query)
        
        data = cursor.fetchone()
        print("data fetched from the database :",data)

        if data:
                
                ( username, password, email, phonenumber, street, society, landmark,
                city, state, pincode,Name,emp_id, emp_name, company_name, designation, 
                date_of_joining,Name,aadharcard_number,pancard_number )= data
                
            
        return render_template('profile.html',username=username,password=password,email=email,
                                              phonenumber=phonenumber,street=street,society=society, 
                                              landmark=landmark,city=city,state=state,
                                            pincode=pincode,emp_id=emp_id, emp_name=emp_name,
                                            company_name=company_name,designation=designation,date_of_joining=date_of_joining,Name=Name, 
                                            aadharcard_number=aadharcard_number,pancard_number=pancard_number)
        
    else:
        return redirect(url_for('login'))
    



if __name__ == '__main__':
    app.run(debug=True)   







    