# Imports
from flask import (Flask,
                   redirect,
                   url_for,
                   request,
                   render_template)
import mysql.connector
import json
from flaskext.mysql import MySQL

app = Flask(__name__,template_folder="templates")
app.config['MYSQL_DATABASE_USER'] = os.environ.get('MYSQL_USER', None)
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('MYSQL_PASS', None)
app.config['MYSQL_DATABASE_DB'] = os.environ.get('MYSQL_DB', None)
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('MYSQL_HOST', None)
mysql = MySQL(app)
# Connecting to Sql
# config = {
#     'user': 'root',
#     'password':  'root',
#     'host': 'db',
#     'port': '3306',
#     'database': 'Employee'
# }

connection = mysql.connect()
cursor = connection.cursor()

# Home Method
@app.route("/", methods=['GET','POST'])
def home():

    # Post request
    if request.method == "POST":

        # Get Data from Form
        name = request.form['name']
        job = request.form['job']
        salary = request.form['salary']

        # Insert into employee Table
        addEmployee = ("INSERT INTO employee "
              "(name, job, salary) "
              "VALUES (%(name)s, %(job)s, %(salary)s)")
        
        dataEmployee = {
            'name': name,
            'job': job,
            'salary': salary,
        }
        cursor.execute(addEmployee,dataEmployee)
        connection.commit()

    # Get All Employees
    getEmployees = "select * from employee"
    cursor.execute(getEmployees)
    AllEmployees = cursor.fetchall()

    # Render Home Page
    return render_template('home.html',allEmployees=AllEmployees)

# Delete Method
@app.route("/delete", methods=['POST'])
def delete():

    # Get ID from form
    id_ = (request.form['id'],)
    # Delete From employee Table
    deleteEmployee = """ Delete from employee where id = %s """
    cursor.execute(deleteEmployee,id_)
    connection.commit()

    # Redirect to Home page
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0')
