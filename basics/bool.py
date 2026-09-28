enter_age = input("Please enter your age: ")
license_input = input("Do you have a driving license? (yes/no): ")
age = int(enter_age)
has_license = license_input.lower() == "yes"
if age >= 18 and has_license:
    print("You are eligible to drive.")
elif age >= 18 and not has_license:
    print("You are not eligible to drive because you do not have a driving license.")
else:
    print("You are not eligible to drive because you are under 18 years old.")  