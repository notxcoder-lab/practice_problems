#Objective: Determine whether a given integer is prime.
number = int(input("Enter a number: "))
for i in range(2,number-1):
    if number%i==0:
        print("This is a prime number")
else:
    print("This is not a prime number")