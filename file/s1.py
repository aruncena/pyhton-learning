import subprocess
import re
file_name = input("Enter the file name: ")
if file_name == "nginx.log":
    print ("Nginx log file found")
else:
    subprocess.run(["touch", "nginx.log"])
    print ("Nginx log file created")
# with open("nginx.log", "r") as f:
#     f.write("\nNginx log file created in the current directory")
#     print ("Nginx log file created and written to", "nginx.log")
with open("nginx.log", "r") as f:
    file_contents = f.read()
    list_of_lines = file_contents.splitlines()
    print ("Nginx log file contents:\n", list_of_lines[5])

pattern = r"nginx"
print(re.fullmatch(pattern, list_of_lines[5]))          