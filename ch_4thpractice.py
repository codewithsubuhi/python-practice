student = {
    "name":"subuhi",
    "age":20,
    "city":"sitamarhi",
}
print(student)
#2nd val
student = {
    "name":"subuhi",
    "age":20,
}
print(student["name"])
print(student["age"])
#3rd 
info = {
    "name":"subuhi",
    "learning":"coding",
    "age":19,
    "is_adult":"true",
    "marks":94.4,
}
print(info)
#4th dict. key
student = {
    "name":"subuhi",
    "subject":{
        "phy":97,
        "chem":98,
        "math":95,
    }
}
print(len(student))
#5th dict. values
student = {
    "name":"subuhi khan",
    "subject":{
        "phy":97,
        "chem":98,
        "math":95,
    }
}
print(list(student.values()))
#6th dic.get ("key")
student={
    "name":"subuhi",
    "age":20
}
print(student.get("name"))
print(student.get("age"))
print(student.get("city"))
#7th dict.update
student={
    "name" :"subuhi khan",
    "subject":{
        "phy":97,
        "chem":98,
        "math":95,
    }

}
new_dict={"name":"sohail","age":16}
student.update(new_dict)
print(student)
#8th set in python
collection={1,2,3,4}
print(collection)
print(type(collection))
#or
collection={1,2,2,2,"hello","world","world"}
print(collection)
print(type(collection))
print(len(collection))
#9th set.add(el)
collection=set()
collection.add(1)
collection.add(2)
collection.add(2)
print(collection)
#10 set.remove(el)
collection=set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.remove(1)
print(collection)
#11th set.clear()
collection=set()
collection.add(1)
collection.add(2)
collection.add("apna college")
collection.add((1,2,3))
collection.clear()
print(len(collection))
#12th set.pop()
collection={"hello","apnacollege","world","coding","python"}
print(collection.pop())
print(collection.pop())
print(collection.pop())
#(i)let's prectice
dictionary={
    "cat":"a small animal","table":["a piece of furnitrue","list of fact & figures"]
}
print(dictionary)
#(ii)pending
#(iii)
marks ={}
x=int(input("enter phy:"))
marks.update({"phy":x})
x=int(input("enter math:"))
marks.update({"math":x})
x=int(input("enter chem:"))
marks.update({"chem":x})
print(marks)
#(iv)
values={9,9.0}
print(values)#9
values={9,9.25}
print(values)
values={9,"9.0"}
print(values)
#happy ending

