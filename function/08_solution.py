def make_dict(**arg):
    dicto = {}
    for key,value in arg.items():
        dicto[key] = value
    return dicto




user_dict= make_dict(name="shaktiman", power="lazer" ,enemy =  "thanos", equipment = "sword")
new_dict = make_dict(name  = "ANURAG", power ="coding")
print(new_dict)
print(user_dict)