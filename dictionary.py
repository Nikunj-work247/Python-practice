student = {
    "name": "Nikunj",
    "age": 25,
    "city": "Indore"
}

user = {
    "name": "Nikunj",
    "age": 25
}

print(user["name"])
print(user["age"])

print(user.get("name"))
print(user.get("email"))

user = {
    "name": "Nikunj",
    "age": 25
}

user["age"] = 26

print(user)

user = {
    "name": "Nikunj",
    "age": 25
}

print(user.get("name"))
print(user.get("email"))
print(user.keys())

#Updating 
user.update({
    "age": 26,
    "city": "Indore"
})

print(user)

user.update({
    "age": 26,
    "city": "Indore"
})

print(user)