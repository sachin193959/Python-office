

a=input("Enter a first num:-")
b=input("Enter a second num:-")


try:
    c = int(a) + int(b)
except:
    print("Please enter inteder value")
else:
    print("Addition is:",int(a) + int(b))
finally:
    print("Anyway its done")

    a = input("Enter a first num:-")
    b = input("Enter a second num:-")
    print("Addition is:",int(a) + int(b))
