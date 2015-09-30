import re
while True:
    password = raw_input("Enter the desired Password: ")
    if len(password) < 1:
        print
        print("You are taking me in the mailing")
        print


    pw_score = 0

    if re.search(r'[A-Z]', password):
        pw_score = pw_score + 1
    if re.search(r'[a-z]', password):
       pw_score = pw_score + 1
    if re.search(r'[0-9]', password):
        pw_score = pw_score + 1
    if re.search(r' ', password): 
        pw_score = pw_score + 10

    if pw_score == 0:
        print("Password is non-existant")
    if pw_score <= 2 and pw_score > 0:
        print("Password is Weak")
    if pw_score == 3 and len(password) > 6:
        print("Password is Medium")
    if pw_score == 3 and len(password) < 6:
        print("Password is Weak")
    if pw_score > 3 and len(password) < 6:
        print("Password is Weak")
    if pw_score > 3 and len(password) < 18 and len(password) > 6:
        print("Password is Medium")
    if pw_score > 3 and len(password) > 18:
        print("Password is Strong") 

    break 
