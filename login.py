def strong_password(password1):
    if len(password1)>=8:
        if "a" in password1 or "b" in password1 or "c" in password1 or "d" in password1 or "e" in password1 or "f"  in password1 or "g" in password1 or "h" in password1 or "i" in password1 or "j" in password1 or "k" in password1 or "l" in password1 or "m" in password1 or "n" in password1 or "o" in password1 or "p" in password1 or "q" in password1 or "r" in password1 or "s" in password1 or "t" in password1 or "u" in password1 or "v" in password1 or "w" in password1 or "x"in password1 or "y" in password1 or "z":
            if  "A" in password1 or "B" in password1 or "C" in password1 or "D" in password1 or "E" in password1 or "F"  in password1 or "G" in password1 or "H" in password1 or "I" in password1 or "J" in password1 or "K" in password1 or "L" in password1 or "M" in password1 or "N" in password1 or "O" in password1 or "P" in password1 or "Q" in password1 or "R" in password1 or "S" in password1 or "T" in password1 or "U" in password1 or "V" in password1 or "W" in password1 or "X"in password1 or "Y" in password1 or "Z":
                if "1" in password1 or "0" in password1 or "2" in password1 or "3" in password1 or "4" in password1 or "5" in password1 or "6" in password1 or "7" in password1 or "8" in password1 or "9":
                    if "_" in password1 or "@" in password1 or "#" in password1 or "&" in password1 or "*" in password1 or "!" in password1 or "$" in password1 or "?" in password1:
                        return True
                    else:
                        return("you need to add speacial character")
                else:
                    return("you have to add numeric character")
            else:
                return(" you have to add capital letter")
        else:
            return("you need to add small chacter")
    else:
       return(" your number should be grater or equal to 8")
def asking_password():
    i=0
    while True:
        password1=input("enter your password")
        password2=input(" confirm your password")
        if password1==password2:
            result=strong_password(password1)
            if result==True:
                return password1
            else:
                print(result)
                continue
        else:
            print("your both password should be match!")
            continue
import json
def readJsonfile(fileName,user_name):
    with open("data.json","r") as f:
        data=json.load(f)
        print(data)
        list_user=data["user"]
        for i in list_user:
            if user_name==i["name"]:
                return True
        return data
def user_exit(fileName):
    with open(fileName,"r") as f:
        data=json.load(f)
        list_user=data["user"]
        for i in list_user:
            if user_name==i["name"] and password==i["password"]:
                return True
        return False
def writejsonfile (fileName,dataTowrite):
    with open(fileName,"w") as f :
        json.dumps(dataTowrite)
        json.dumps(dataTowrite,f,indent=4)
def printing_details(dict1):
    for i,j in dict1.items():
        if i=="name":
            print(i,":",j)
        if i=="display pic":
            a=dict1[i]
            for k,l in a.items():
                print(k,":",l)
user1=input("enter login or signup for signup press1 and for login press 2:")
if user1=="1":
    user_name=input("enter your name,,,,,,","\U0001F600")
    password=asking_password()
    dict1={"name":user_name,"password":password}
    dataFromjson=readJsonfile("data.json",user_name)
    if dataFromjson==True:
        print("already exist")
    else:
        dict1={"name":user_name,"password":password}
        print(user_name,"your login succesfully")
        dataFromjson=readJsonfile("data.json",user_name)
        bio=input("enter your bio")
        date_of_birth=input("what is your D.O.B")
        hobbies=input("what is your hobbies")
        gender=input("what is your gender")
        dict2={"bio":bio,"date_of_birth":date_of_birth,"hobbies":hobbies,"gender":gender}
        dict1.update({"profile":dict2})
        dataFromjson["user"].append(dict1)
        dataTojson=writejsonfile("data.json",dataFromjson)
        printing_details(dict1)
elif user1=="2":
    user_name=input("enter your name,,,,","\U0001F600")
    password=input("enter your password,,,,,")
    userexsist=user_exit("data.json")
    if userexsist==True:
        print(user_name,"your login successfully")
    else:
        print("user is not exsist")
else:
    print("invailed input")
