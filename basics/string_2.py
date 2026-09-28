### List
names = ["arun", "kumar", "cena"]

servers = ["192.168.1.1", "192.168.1.1", "192.168.1.2", "192.168.1.3"]

print("List of nams:", names)

names[2] = "new name"

print(names)

names.append("lastname")
print(names)

print("List of server:", servers)

### tuple
db_config = ("server1", "192.168.1.1", "5432")
print(db_config)
# db_config[0]="server2"
# print(db_config)

### Sets
servers = {"192.168.1.1", "192.168.1.1", "192.168.1.2", "192.168.1.3"}
print(servers)
servers.add("192.168.1.4")
print(servers)

### dict
employee = {
    "name": "Arun",
    "grade": "B",
    "Dept": "IT"
}
print(employee)
print(employee["name"])

employee["Dept"] = "Dev"
print(employee)