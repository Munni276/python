#tuples are immutable,meaning they cannot be changed after they are created.they are defined using parenthasis
numbers =(10,20,20,30,20)

print(numbers.count(20))

 #index

numbers = (10,20,30,40)

print(numbers.index(30))

numbers =(10,20,30,40)


print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python
#set is a collection of unique values that is unordered and mutable
numbers ={10,20,30,20,10}

print(numbers)

#add values to a set
subjects ={"python","java"}

subjects.add("SQL")

print(subjects)

#remove values from a set
subjects.remove("java")

print(subjects)

#sets do not allow the duplicate values
numbers= {1,2,2,3,3,4}

print(numbers)

#dictionaries in python
#dictionary is a collection of key-value pairs that is ordered and mutable
student={
    "name": "Manu",
    "age": "20",
    "course": "python"
}

print(student)

#access elements in dictionary
print(student["name"])
print(student["age"])
print(student["course"])

#add new data to a dictionary
student["city"] = "Vijayawada"

print(student)

## Dictionaries are unordered collections
student={
    "name": "Manu",
    "age": 20,
    "course":"python"
    }
print(student.keys())
#keys() returns all the keys in the dictionary

print(student.items())
#items() returns all key-value pairs

print(student.get("name"))
#get()returns the value of specified key

print(student. values())
#values() returns all the values in the dictionary

student.update({"age":22})
#update()updates the value of specified key

print(student)

student.pop("age")
#pop()removes the specified key and its value

print(student)
#popitem() removes the last inserted key-value pair
student={
    "name": "Manu",
    "age": 20,
    "course":"python"
}

student.popitem()

print(student)

student={
    "name":"Manu"
}

student.setdefault("age",21)

print(student)
 