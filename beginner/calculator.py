def add(m,n):
    return m + n

def sub(m,n):
    return m - n

def mul(m,n):
    return m * n

def div(m,n):
    m / n

print("Please select operation -\n"
        "1. Add\n"
        "2. Subtract\n"
        "3. Multiply\n"
        "4. Divide\n")

sel = int(input("Select operations from 1-4: "))

m = int(input("Enter first number: "))
n = int(input("Enter second number: "))

if sel == 1:
    print(m, "+", n, "=", add(m,n))
elif sel == 2:
    print(m, "-", n, "=", sub(m,n))
elif sel == 3:
    print(m, "*", n, "=", mul(m,n))
elif sel == 4:
    print(m, "/", n, "=", div(m,n))
else:
    print("Invalid input")