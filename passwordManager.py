from cryptography.fernet import Fernet

# def wKey():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)    this was the method to write the key. 

#this project is a password manager which creates a new text file called passwords.txt if
#it doesn't already exist and if it does exist it writes on the file. It writes 
#your passwords down in a scrambled format which can only be viewed once you press
#the view option on the terminal when you run the code. It also has a method which 
#generates a key which has been commented out but needs to be uncommented to make
#a new key on a new system. There is also the method below to load the key once it 
#has been created. This key will eventually be used to create a master password 
#which will be needed to run the code fully.

def lKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = lKey() 
fer = Fernet(key)



        
    

   

#my functions 
def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode()).decode()) + "\n")

#now ask what state they want. The state to add a new password or the state to display the passwords.
while True:
    state = input("Do you want to add a new password or view your passwords? (*add* to add *view* to view *q* to quit) ").lower()
    if state == "q":
        break

    if state == "view":
        view()
    elif state == "add":
        add()
    else:
        print("Not valid option")
        continue