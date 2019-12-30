num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


def add():
    add_res = num1 + num2
    print(add_res)


def mul():
    mul_res: int = num1 * num2
    print(mul_res)


def div():
    div_res = int(num1 / num2)
    print(div_res)


def subr():
    sub_res: int = num1 - num2
    print(sub_res)


print("Select the number of operation of your choice:")
vangurathu = input("1. Addition: 2. Multiplication  3. Division  4. Subtraction: ")
if vangurathu == "1":
    print("you have selected addition")
    add()
elif vangurathu == "2":
    print("you have selected multiplication")
    mul()
elif vangurathu == "3":
    print("you have selected Division")
    div()
elif vangurathu == "4":
    print("you have selected Subtraction")
    subr()
else:
    print("Invalid input: enter 1 or 2 or 3 or 4")
