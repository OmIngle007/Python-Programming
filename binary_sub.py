def binary_subtraction(a, b):
    if len(a) < len(b):
        a, b = b, a

    b = b.zfill(len(a))

    result = ""
    borrow = 0

    for i in range(len(a) - 1, -1, -1):  
        a_digit = int(a[i])
        b_digit = int(b[i])

        sub = a_digit - b_digit - borrow

        if sub == 0:
            result = "0" + result
            borrow = 0
        elif sub == 1:
            result = "1" + result
            borrow = 0
        elif sub == -1:
            result = "1" + result
            borrow = 1
        elif sub == -2:
            result = "0" + result
            borrow = 1

    result = result.lstrip("0")

    return result if result != "" else "0"

a = str(input("Enter Binary Input a: " ))
b = str(input("Enter Binary Input b: "))

print(binary_subtraction(a, b)) 
