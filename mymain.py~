from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route('/')
def signup():
      return render_template('signup.html')
@app.route('/', methods=['POST'])
def confirm_signup():
	username = request.form['username']
	password= request.form['password']
	verify_password= request.form['verify_password']
	email= request.form['email']
	errors = { "username": "", "password": "", "verify_password": "", "email" : ""}

	if len(username)==0 or len(username) not in range(3, 21) or username.find(' ')!=-1:
		errors["username"] = "The '{0}' have not to be empty and has no space.The length has not to be out of the range 3 to 21".format("username")
		return errors
		#return errors["username"]
             #return valid    
             #return redirect("/?error=" + error)
	if len(password) not in range(3, 21) or password.find(' ')!=-1:
		errors["password"] = "The '{0}'length has not to be out of the range 3 to 21 and '{1}' must match the given '{2}'".format("password", "verify_password", "password")
		return errors
		#return errors["password"]
            #return valid 
            #return redirect("/?error=" + error)
	if verify_password!=password:
		errors["verify_password"] = "The '{0}'must match the entered '{1}'".format("verify_password",  "password")
		return errors

	if len(email) not in range(3, 21) or email.find("@")==-1 or email.find(".")==-1 or email.find(" ")!=-1:
		errors["email"] = "The '{0}'must contain '{1}' has no space .It must be 3 to 21 character length ".format("email","@ .")
		return errors
                  ### case the email is not provided or the email ist left empty
	else:
		if len(email)==0:
			errors['email']==''
			return errors
			#return errors["email"]
			
	
	if errors=={ "username": "", "password": "", "verify_password": "", "email" : ""}: # case no errors == successful signed up

		return render_template('confirm.html', email=email, username=username)
		#case errors == at least field has errors
	else:
		u_error=(list(errors.values()))[0]
		p_error=(list(errors.values()))[1]
		pv_error=(list(errors.values()))[2]
		em_error=(list(errors.values()))[3]
		return render_template('confirmss.html',u_error=u_error, p_error=p_error, pv_error=pv_error, em_error=em_error,username=username, email=email)
		#return render_template('confirm.html',u_error=u_error,p_error=p_error,pv_error=pv_error,em_error=em_error, email=email, username=username)
app.run()