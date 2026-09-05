print("simple calculater program")
print("ooperatiooons:+ - * /")
# taking input
num1 = float(input("enter first number: "))
op=input("enter operator: ")
num2 = float(input("enter second number: "))

# calculation
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
       result = num1 / num2
    else:
        result = "error! division by zero"
else:
    result = "invalid operator"
    
# output
print("result:",result)            
     