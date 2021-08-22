# The password manager version 2
# Menu
def Menu():
    os.system("cls")
    print("==============================")
    print("The password manager system")
    print("==============================")
    print("Menu")
    print("1. Enter the login/password")
    print("2. Dispaly the login/password")
    print("3. Modify the password")
    print("4. Delete the login/password")
    print("5. End the system")
    Choice()
# Choice
def Choice():
    while True:
        choice=float(input("Please choice the option:"))
        if choice==1:
            Inputdata()
            Menu()
            break
        elif choice==2:
            Display()
            Menu()
            break
        elif choice==3:
            Modify()
            Menu()
            break
        elif choice==4:
            Delete()
            Menu()
            break
        elif choice==5:
            input("Thanks for use, Enter to close program")
            break
        # elif choice =="":
        #     print("Wrong type, Please choice anain")
        else:
            print("Wrong type, Please choice anain")
# Input data
def Inputdata():
    data=Readdata()
    data_I=ast.literal_eval(data)
    while True:
        login=input("Please keyin the Login(keyin Enter to return Menu):")
        while login in data_I:
            print("There are same login, please check")
            break
        while login =="":
            #input("End type, keyin to return the Menu")
            return
        while login not in data_I:                
            if login !="":
                password=input("Please keyin the password:")
                data_I[login]=password
                with open("password manager.txt", mode="w", encoding="UTF-8-sig") as pw:
                    datafile_I=str(data_I)
                    pasw=pw.write(datafile_I)
                    continue
# Read data
def Readdata():
    file="password manager.txt"
    while not os.path.exists(file):
        with open("password manager.txt", mode="w", encoding="UTF-8-sig") as f:
            data_F={}
            datafile_F1=f.write(str(data_F))
            return datafile_F1
    else:
        with open("password manager.txt", mode="r", encoding="UTF-8-sig") as ps:
            datafile_F2=ps.read()
            if datafile_F2 =="":
                data2={}
                return data2
            else:
                return datafile_F2
# Display data
def Display():
    file=Readdata()
    data=ast.literal_eval(file)
    while True:
        enter=input("Please keyin the login(keyin Enter to return Menu):")
        while enter in data:
            print("login:{}\tpassword:{}".format(enter,data[enter]))
            break
        while enter not in data:
            print("The loging isn't exist")
            break
        while enter =="":
            #input("End to search, key enter to return Menu")
            return
            # break
# Modify data
def Modify():
    file=Readdata()
    data=ast.literal_eval(file)
    while True:
        enter=input("Please keyin the login(keyin Enter to return Menu):")
        while enter in data:
            print("Original password:", data[enter])
            newpw=input("Please keyin the new password:")
            data[enter]=newpw
            with open("password manager.txt", mode="w", encoding="UTF-8-sig") as f:
                data2=str(data)
                final=f.write(data2)
                break
        while enter not in data:
            print("The loging isn't exist")
            break
        while enter =="":
            #input("End to modify, key Enter to retrun Menu")
            return
# Delete data
def Delete():
    file=Readdata()
    data=ast.literal_eval(file)
    while True:
        enter=input("Please keyin the login(keyin Enter to return Menu):")
        while enter =="":
            return
        while enter not in data:
            input("The login isn't exist. Pleaes keyin again")
            break
        while enter in data:
            print("Orignal password:", data[enter])
            yn=input("Sure to delete? (Y/N?)")
            while yn=="y" or yn=="Y":
                del(data[enter])
                input("The login is delete")
                with open("password manager.txt", mode="w", encoding="UTF-8-sig") as ps:
                    file=ps.write(str(data))
                    break
                break
            while yn=="n" or yn=="N":
                print("The login is survival")
                break
            break
        #while enter not in data:
            #input("The login isn't exist. Please keyin again")
            #break
# Main Program
import ast, os
os.system("cls")
Readdata()
Menu()