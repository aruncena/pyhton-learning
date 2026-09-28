text = "Hello from python"
print(text.split()[2])

count = len(text)
print("total words in text:", count)

caps = text.upper()
print(caps)

lower = text.lower()  
print(lower)

replace = text.replace("python", "Linux")
print(replace)

split = text.split()
print(split)

arn = "arn:partition:service:region:account-id:resource-type:resource-id"
new_format = arn.split("-")
print(new_format)

arn_filed = arn.split("-")[1]
print(arn_filed)
