import json

with open(r'execercise/data.json') as f:
    company_data = json.load(f)
    print(company_data["servers"][0]["services"])
svc_details = company_data["servers"][0]["services"]

for svc in svc_details:
    if svc == "nginx":
        print("Nginx is running")
    elif svc == "docker":
        print("Docker is running")
    else:
        print("Please choose a valid service name, either nginx or docker")               
