print("welcome User.To set up Mac OS Catlina input the following.")
username=input("Input Username:")
password=int(input("Input Password:"))
email=input("Input Email:")
age=int(input("Input Age:"))
gender=input("Input Gender:")
date_of_birth=input("Input Date Of Birth:")
print("Loading Please Wait...")
def setup(username,password,email,age,gender,date_of_birth):
    print(f"username={username} password={password} email={email} age={age} gender={gender} date of birth={date_of_birth}")

setup(username,password,email,age,gender,date_of_birth)
print("Setup Complete")