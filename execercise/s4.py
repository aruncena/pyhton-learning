import re
branches = [
    "main",
    "develop",
    "feature/login",
    "feature/payment",
    "bugfix/connection",
    "feature/dashboard",
    "release/v1.2.0"
]

pattern = r"feature/.*"
matches = []
for branch in branches:
    if re.match(pattern, branch):
        matches.append(branch)
print("Branches matching the pattern 'feature/.*':")
for match in matches:
    print(match)  