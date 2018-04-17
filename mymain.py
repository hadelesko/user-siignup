from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route('/')
def signup():
      return render_template('signup.html')
#def em_valid():
	

@app.route('/', methods=['POST'])
def confirm_signup():
	username = request.form['username']
	password= request.form['password']
	verify_password= request.form['verify_password']
	email= request.form['email']
	errors = { "username": "", "password": "", "verify_password": "", "email" : ""}
	
	u_error= ""      #errors_massage[0]   #=(list(errors.values()))[0]
	p_error= ""      #errors_massage[1]   #=(list(errors.values()))[1]
	pv_error= ""     #errors_massage[2]   #=(list(errors.values()))[2]
	em_error= ""     #errors_massage[3]   #=(list(errors.values()))[3]
	errors_massage=[]
	if len(username)==0 or len(username) not in range(3, 21) or username.find(' ')!=-1:
		#errors["username"] = "The '{0}' have not to be empty and has no space.The length has not to be out of the range 3 to 21".format("username")
		u_error="The '{0}' have not to be empty and has no space.The length has not to be out of the range 3 to 21".format("username")
		errors_massage.append(u_error)
		#return u_error
	else:
		u_error=""
		errors_massage.append(u_error)
		#return u_error

	if len(password) not in range(3, 21) or password.find(' ')!=-1:
		#errors["password"] = "The '{0}'length has not to be out of the range 3 to 21".format("password")
		p_error= "The '{0}'length has not to be out of the range 3 to 21".format("password")
		p_error
		errors_massage.append(p_error)
		#return p_error
	else:
		p_error=""
		errors_massage.append(p_error)
		#return p_error

	if verify_password!=password:
		pv_error="The '{0}'must match the entered '{1}'".format("verify_password", "password")
		errors_massage.append(pv_error)
		#return pv_error
	else:
		pv_error=""
		errors_massage.append(pv_error)
		#return pv_error

	if len(email)==0:
		em_error=""
		errors_massage.append(em_error)
		#return em_error
	else:
		if len(email)<3 or len(email)>20:
			em_error="The '{0}'must contain '{1}' has no space .It must be 3 to 21 character length ".format("email","@ .")
			errors_massage.append(em_error)
			#return em_error
		else:
			if email.find("@")==-1 or email.find(".")==-1 or email.find(" ")!=-1:
				em_error=emr="The '{0}'must contain '{1}' has no space .It must be 3 to 21 character length ".format("email","@ .")
				errors_massage.append(em_error)
				#return em_error
			else:
				em_error=""
				errors_massage.append(em_error)
				#return em_error

	if len(errors_massage[0])==0 and len(errors_massage[1])==0 and len(errors_massage[2])==0 and len(errors_massage[3])==0:
		#if len(u_error)==0 and len(p_error)==0 and len(pv_error)==0 and len(em_error)==0:
		return render_template('confirm.html', email=email, username=username)

		#case errors == at least field has errors
	else:
		return render_template('confirmss.html', u_error=errors_massage[0], p_error=errors_massage[1], pv_error=errors_massage[2], em_error=errors_massage[3], username=username, email=email)
app.run()