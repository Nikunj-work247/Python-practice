import json

def read_json_file(filename):

    with open(filename, "r") as file:
        data = json.load(file)

    return data


user_data = read_json_file("user.json")

print(user_data)
print(type(user_data))