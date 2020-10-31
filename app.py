from addition import add
print(2 + 3)
from subtraction import subtract
print(10-6)
from multiplication import multiply
print(25*10)
from division import divide
print(4/2)





print("Select a number Champ!")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    yourChoice = input("Enter your choice(1/2/3/4): ")
    if yourChoice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if yourChoice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif yourChoice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif yourChoice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))   
        elif yourChoice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid input")       