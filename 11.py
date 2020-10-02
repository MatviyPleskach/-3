print("Test Security Programm")
print("Welcome")
login = input("Login:")
if login == "admin" :
   print ("Enter your password")
else:
   print("Check your password or login")


password = input("Password:")
if password == "1234qwer" :
   print ("Acces allowed")

else:
   print ("Acces denied")
   exit ()
