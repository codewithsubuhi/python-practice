#lenth
str = "apna"
len = len (str)
print(len)
#indexing
str = "apna college"
ch = str[2]
print(ch)
#slicing 
str = "apna college"
print(str[1:4])
#negative index
str = "apple"
print(str[-5:-2])
#str.endwith
str = "i am studing python from apnacollege"
print(str.endswith("ege"))
print(str.endswith("app"))
#capitalize 
str = "i am subuhi"
print(str.capitalize())

str = "i am studing python from apnacollege"
str = str.capitalize()
print(str)
#replace
str = "i am studing python from apnacollege"
print(str . replace ("python ","javascript"))

str = "subuhi"
print(str.replace("subuhi","sohail"))
#find
str = "i am studing python from apnacollege"
print(str. find("o"))
print(str.find("m"))
#count
str = "i am from studing python from apnacollege"
print(str.count("from"))
print(str.count("o"))
#prectice l_2
name = input("enter your nam")
print("length of your name is len (name)")

str = "hi,$ i am $ symbol $99.99"
print(str.count("$"))
#conditional statement 
age = 21 
if (age >= 18):
    print("can vote & apply for license")
#second
    light = "green"
    if (light == "red"):
        print("stope")
    elif(light =="green"):
        print("go")
    elif(light == "yellow"):
        print("look")
    #third
    num = 5
    if (num > 2):
        print("greater than 2")
    elif (num > 2):
        print("greater than 3")
#forth
light = "pink"
if (light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")
    print("end of code")
    #5th
    age = 14
    if (age >= 18):
        print ("can vote")
    else:
        print("cannot vote")

    age = 24
    if (age >= 18):
        print("can vote")
    else:
        print("cannot vote")
        #6th nesting
        age = 95
        if (age >= 18):
            if (age >= 80):
                print("cannot drive")
        else:
            print("can drive")
            #lets prectice(1)
            num = int (input("enter number:"))
            if (num%2==0):
                print("even")
            else:
                print("odd")

        


    


