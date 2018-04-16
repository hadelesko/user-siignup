def confirm_signup():
      username = 'username'
      password= 'password'
      verify_password= 'verify_password'
      email= 'email'
      errors = { "username": "", "password": "", "verify_password": "", "email" : ""}
      b_errors=[]
      if len(username)==0 or len(username) not in range(3, 21) or username.find(' ')!=-1:
          errorsu = "The '{0}' have not to be empty and has no space.The length has not to be out of the range 3 to 21".format("username")
          return b_errors.append(errorsu)
          #return errors, b_errors
          #return errors["username"]
       #return valid    
       #return redirect("/?error=" + error)
      if len(password) not in range(3, 21) or password.find(' ')!=-1:
          errorsp = "The '{0}'length has not to be out of the range 3 to 21 and '{1}' must match the given '{2}'".format("password", "verify_password", "password")
          return b_errors.append(errorsp)
          #return b_errors
          #return errors["password"]
          #return valid 
          #return redirect("/?error=" + error)
      if verify_password!=password:
            errorspv= "The '{0}'must match the entered '{1}'".format("verify_password",  "password")
            return b_errors.append(errorspv)
            

      if len(email) not in range(3, 21) or email.find("@")==-1 or email.find(".")==-1 or email.find(" ")!=-1:
            errorse= "The '{0}'must contain '{1}' has no space .It must be 3 to 21 character length ".format("email","@ .")
            return b_errors.append(errorse)
            #return errors , b_errors
      
