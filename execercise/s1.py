
# import re

# pattern = r"\d+"
log_path = "./log.txt"
with open(log_path, "r") as file:
    content = file.read()
    split = content.split( )
    # matches = re.findall(pattern, content)
    # print(matches)
    print(f"The date is: {split[0]}. and time is {split[1]} log level is {split[2]} from service name {split[3]} {split[4]} {split[5]} {split[6]} and server IP is {split[7]}")
    