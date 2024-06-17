print("1-Add")
print("2-Subtract")
print("3-Multiply")
print("4-Divide")
operation=int(input("choose operation: "))
if(operation in [1,2,3,4]):
    num1=(float(input("Enter the first number: ")))
    num2=(float(input("Enter the second number: ")))
    if(operation == 1):
        result=num1+num2
    elif(operation == 2):
        result=num1-num2
    elif(operation == 3):
        result=num1*num2
    elif(operation == 4):
        result=num1//num2 
else:
    print("Invalid operation") 
print("result of operation is {}".format(result))