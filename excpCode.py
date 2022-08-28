
a=5
b=2

try:
    print("File Opened")
    print(a/b)
    k = int(input("Enter a Number \n"))
    print(k)
except ZeroDivisionError as e:
    print("Hey! You can't divide number by Zero", e)

except ValueError as e:
    print("Hey! Invalid Input", e)

except Exception as e:
    print("Hey! Something Went Wrong", e)

finally:
    print("File Closed")