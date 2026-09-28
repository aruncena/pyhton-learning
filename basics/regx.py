import re
# text = "hello world from python"
# pattern = r"world"

# result = re.search(pattern, text)
# print(result.group())  # Output: world

pattern = r"missing"
file_path = "./sample.txt"
with open(file_path, "r") as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            print(match.group())