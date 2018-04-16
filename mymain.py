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
	errors_massage=[]
	u_error= ""      #errors_massage[0]   #=(list(errors.values()))[0]
	p_error= ""      #errors_massage[1]   #=(list(errors.values()))[1]
	pv_error= ""     #errors_massage[2]   #=(list(errors.values()))[2]
	em_error= ""     #errors_massage[3]   #=(list(errors.values()))[3]
	if len(username)==0 or len(username) not in range(3, 21) or username.find(' ')!=-1:
		#errors["username"] = "The '{0}' have not to be empty and has no space.The length has not to be out of the range 3 to 21".format("username")
		ur="The '{0}' have not to be empty and has no space.The length has not to be out of the range 3 to 21".format("username")
		u_error=ur
		errors_massage.append(ur)
		#return errors, errors_massage
	else:
		errors["username"]=""
		ur=""
		u_error=ur
		errors_massage.append(ur)
		return errors, errors_massage

	if len(password) not in range(3, 21) or password.find(' ')!=-1:
		#errors["password"] = "The '{0}'length has not to be out of the range 3 to 21 and '{1}' must match the given '{2}'".format("password", "verify_password", "password")
		pr= "The '{0}'length has not to be out of the range 3 to 21 and '{1}' must match the given '{2}'".format("password", "verify_password", "password")
		p_error=pr
		return p_error
	else:
		errors["password"] = ""
		pr=""
		p_error=pr
		return p_error

	if verify_password!=password:
		#errors["verify_password"] = "The '{0}'must match the entered '{1}'".format("verify_password",  "password")
		pvr="The '{0}'must match the entered '{1}'".format("verify_password",  "password")
		pv_error=pvr
		return pv_error
	else:
		errors["verify_password"] = ""
		pvr=""
		pv_error=pvr
		return pv_error

	if len(email) not in range(3, 21) or email.find("@")==-1 or email.find(".")==-1 or email.find(" ")!=-1:
		#errors["email"] = "The '{0}'must contain '{1}' has no space .It must be 3 to 21 character length ".format("email","@ .")
		emr="The '{0}'must contain '{1}' has no space .It must be 3 to 21 character length ".format("email","@ .")
		em_error=emr
		return em_error
                  ### case the email is not provided or the email ist left empty
	else:
		if len(email)==0:
			errors['email']==''
			emr=""
			em_error=emr
			return em_error

	if len(u_error)==0 and len(p_error)==0 and len(pv_error)==0 and len(em_error)==0:
		###if errors=={ "username": "", "password": "", "verify_password": "", "email" : ""}: # case no errors == successful signed up
		return render_template('confirm.html', email=email, username=username)
		#case errors == at least field has errors
	else:
		return render_template('confirmss.html',u_error=u_error, p_error=p_error, pv_error=pv_error, em_error=em_error,username=username, email=email)
		#return render_template('confirm.html',u_error=u_error,p_error=p_error,pv_error=pv_error,em_error=em_error, email=email, username=username)
app.run()