# Dictionary
dict1 = {
    "name":"John",
    "age":30,
}
a =dict1["name"]
print(a)
dict1["age"] = 40
print(dict1)

for x, y in dict1.items():
    print(x, y)
# Add A item to dict1
dict1["Address"] = "New York"
print(dict1)

dict1.pop("age")
print(dict1)