user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
if user_age < 18:
    for i in range(user_age):
     print(user_name)
else:
    for i in range(user_age):
        print(i,"x",user_age,"=",i*user_age)    