client = input("Enter your name: ")
n = int(input("Enter 1 for diet and 2 for exercise: "))
m = int(input("Enter 1 to read and 2 to write: "))
if client == "piyush":
    if n == 1:
        if m == 1:
            f = open("piyush Diet")
            content = f.read()
            print(content)
            f.close()
        else:
            x = input("Enter your Diet: ")
            f = open("piyush Diet", "w")
            f.write(x)
            f.close()
            print("Data saved successfully!!")
    else:
        if m == 1:
            f = open("piyush Exercise")
            content = f.read()
            print(content)
            f.close()
        else:
            x = input("Enter your Exercise: ")
            f = open("piyush Exercise", "w")
            f.write(x)
            f.close()
            print("Data saved successfully!!")

elif client == "rahul":
    if n == 1:
        if m == 1:
            f = open("rahul Diet")
            content = f.read()
            print(content)
            f.close()
        else:
            x = input("Enter your Diet: ")
            f = open("rahul Diet", "w")
            f.write(x)
            f.close()
            print("Data saved successfully!!")
    else:
        if m == 1:
            f = open("rahul Exercise")
            content = f.read()
            print(content)
            f.close()
        else:
            x = input("Enter your Exercise: ")
            f = open("rahul Exercise", "w")
            f.write(x)
            f.close()
            print("Data saved successfully!!")

elif client == "modi":
    if n == 1:
        if m == 1:
            f = open("modi Diet")
            content = f.read()
            print(content)
            f.close()
        else:
            x = input("Enter your Diet: ")
            f = open("modi Diet", "w")
            f.write(x)
            f.close()
            print("Data saved successfully!!")
    else:
        if m == 1:
            f = open("modi Exercise")
            content = f.read()
            print(content)
            f.close()
        else:
            x = input("Enter your Exercise: ")
            f = open("modi Exercise", "w")
            f.write(x)
            f.close()
            print("Data saved successfully!!")

else:
    print("Enter valid client name")
