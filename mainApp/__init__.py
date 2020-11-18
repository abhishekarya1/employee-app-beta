from flask import *
import sqlite3
  
app = Flask(__name__) #creating the Flask class object   
 
#my additions

@app.route('/')  
def index():  
    return render_template("index.html"); 

@app.route('/accessVerify')  
def accessVerify():
		return render_template("accessVerify.html")

@app.route('/keyVerify', methods = ["POST","GET"])  
def keyVerify():
	accessKey = request.form["key"]
	if accessKey == '345sdf':
		return render_template("admin.html");
	else: return "Invalid Access Key!"
@app.route('/admin')  
def admin():
	if request.referrer == '/index/accessVerify':
		return render_template("admin.html");
	else: return "Not Permitted" 
    	

@app.route('/registerEmployee')  
def registerEmployee():  
    return render_template("registerEmployee.html"); 

@app.route("/result", methods = ["POST","GET"])
def result():  
    msg = "Looks like the database is not connected :("  
    if request.method == "POST":  
        try:  
            eid = request.form["eid"] 
            name = request.form["name"]  
            address = request.form["address"]
            dob = request.form["dob"]  
            mobile = request.form["mobile"]  
            with sqlite3.connect("employee.db") as con: 
                cur = con.cursor()  
                cur.execute("INSERT into Employees (empID, empName, empAddress, empDOB, empMobileNumber) values (?,?,?,?,?)", (eid, name, address, dob, mobile))  
                con.commit()  
                msg = "Employee record successfully added."
        except:  
            con.rollback()  
            msg = "Unable to add employee record."
        finally:  
            return render_template("success.html", msg = msg)
            con.close()      

@app.route("/view")
def view():  
    con = sqlite3.connect("employee.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("SELECT * FROM Employees")
    rows = cur.fetchall()
    return render_template("view.html", rows = rows)

@app.route('/searchEmployee')  
def searchEmployee():  
    return render_template("searchEmployee.html");

@app.route("/search_result", methods=['GET', 'POST'])
def search_result():
	search_term = request.form["search_term"]
	searchType = request.form["searchType"]
	con = sqlite3.connect("employee.db")  
	con.row_factory = sqlite3.Row  
	cur = con.cursor()
	if searchType == 'name':
		cur.execute("select * from employees WHERE empName LIKE '' || (?) || '%' COLLATE NOCASE", (search_term,))
	elif searchType == 'eid': cur.execute("SELECT * FROM employees WHERE empID == (?)", (search_term,)) 
	elif searchType == 'age': 
		search_term = int(search_term)
		cur.execute("SELECT * FROM employees WHERE ((strftime('%Y', 'now') - strftime('%Y', empDOB)) - (strftime('%m-%d', 'now') < strftime('%m-%d', empDOB))) = (?);", (search_term,))
	rows = cur.fetchall()
	if len(rows) == 0: msg = "No matching records found."
	else: msg = "All records matching the search criteria are: "
	return render_template("search_result.html", msg = msg, rows = rows)

@app.route("/searchByFirstLetter", methods=['GET', 'POST'])
def searchByFirstLetter():
	nameStart = request.form["nameStart"]
	con = sqlite3.connect("employee.db")  
	con.row_factory = sqlite3.Row  
	cur = con.cursor()
	cur.execute("select * from Employees where empName LIKE '' || (?) || '%' COLLATE NOCASE", (nameStart,)) 
	rows = cur.fetchall()
	if len(rows) == 0: msg = "No matching records found."
	else: msg = "All records matching the search criteria are: "
	return render_template("search_result.html", msg = msg, rows = rows)

	

#main
if __name__ =='__main__':  
    app.run(debug = True)  

