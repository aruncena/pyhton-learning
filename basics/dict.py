people = {
    "name": "Alice",
     "age": 25,
      "city": "New York"
}
print(people)
print(people["name"])

people1 = { "profession": "Engineer" }
people.update(people1)
print(people)

people["profession"] = "Doctor" 
print(people)

people.pop("age")
print(people)

people["Pincode"] = "10001"
print(people)