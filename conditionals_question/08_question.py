password = (input("please enter your passwords:"))
pass_len = len(password)
print(pass_len)

if(pass_len <= 6):
    strength = "weak"
elif(pass_len <= 10 ):
    strength = "medium"
else:
    strength = "strong"
    
print("stength of password:",strength)