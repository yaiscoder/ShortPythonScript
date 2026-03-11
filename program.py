print("Welcome")
participants = int(input("How many participants do you want to register?: "))

for i in range(participants):
    name = input("Write your name: ")
    age = int(input("Write your age: "))
    knowledge = input("Do you have basic computer skills? yes/no: ")
    while age <= 15:
        print("Your age is not valid")
        confirm = input("Type 'yes' if you want to try again: ")
        if confirm == 'yes':
            age = int(input("Write your age: "))
        else: 
            print("finished process")
            break
    if knowledge == 'yes' and age > 15:
        print("You can participate in the workshop")
        print("successful registration")
    else:
        print("You do not meet the requirements")
