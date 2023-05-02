def create():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    with open("data.txt", "a") as f:       #opens data.txt to store operation C
        f.write(f"{name},{phone}\n") 
    print("Record created successfully.")

def read():
    phone = input("Enter phone number: ")
    with open("data.txt", "r") as f:
        for line in f:
            rec = line.strip().split(",") #removes white space & access the record in substring form
            if rec[1] == phone:
                print(f"Name: {rec[0]}")
                break
        else:
            print("Record not found.")

def update():
    phone = input("Enter phone number: ")
    name = input("Enter new name: ")
    with open("data.txt", "r") as f:
        lines = f.readlines()             #by using readlines it returns data in list
    with open("data.txt", "w") as f:
        for line in lines:
            rec = line.strip().split(",")
            if rec[1] == phone:
                f.write(f"{name},{phone}\n") #Same process
            else:
                f.write(line)
    print("Record updated successfully.")

def delete():
    phone = input("Enter phone number: ")
    with open("data.txt", "r") as f:
        lines = f.readlines()
    with open("data.txt", "w") as f:
        for line in lines:
            rec = line.strip().split(",")
            if rec[1] != phone:
                f.write(line)        
    print("Record deleted successfully.")


#main CODE (Driver code)
while True:
    choice = input("Enter C to create, R to read, U to update, or D to delete: ")
    if choice == "C":
        create()
    elif choice == "R":
        read()
    elif choice == "U":
        update()
    elif choice == "D":
        delete()
    else:
        print("Invalid choice. Please try again.")