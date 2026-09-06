#"checking a number is positive ,negative or zero"
n = input("Enter a number: ")

if n.startswith("+-"):
    num = int(n[2:])
    print("Positive number: +" + str(num))
    print("Negative number: -" + str(num))

elif int(n) > 0:
    print("Number is positive")

elif int(n) < 0:
    print("Number is negative")

else:
    print("Number is zero")