# create a chatbot 
# def chatbot():
#     print("HLO !  type exit when you done with conversation ")

#     while True:
#         user = input("you : ").lower()
#         if user in ['hii','hello','hye']:           
#             print("Bot : Hllo i 'm chat bot how can i help you !")
#         elif 'how are you' in user:
#             print("Bot : i'm always fine because i am a computer program !")
#         elif 'can you help me !' in user:
#             print("Bot : ofcoursee i am here to help you ")
#         elif 'i want to talk to someone' in user :
#             print("Bot : This is the contact number of our support team.(8420899881) you can contact  them between 10:00AM to 5:30PM ")
            
#         else:
#             print("Bot : some thing is wrong i am not understand what do you want ! ")

# chatbot()

# calculater for arithmetic operations 
# num = int(input("Enter the number : "))
# a = input("add/sub/mul/div :  ")
# num2 = int(input("Enter the number : "))
# if a == "+":
#     print("add :", num + num2 )
# elif a == "-":
#     print("sub :", num - num2)
# elif a == "*":
#     print("mul :",num * num2)
# elif a == "/":
#     print("div :",num / num2)
# else:
#     print("not valid input ")

# task=input("Enter task :")
# while task is "done":
#     print(task)
#     task += 1

def display_menu():
    print("\n simple task mannager : ")
    print("1 . To add task " )
    print("2 . To view list ")
    print("3 . To exit list ")


def add_task(tasks):
    task = input("Enter the task : ")
    tasks.append(task)
    print(f"Task '{task}' added successfully! ")

def view_task(tasks):
    if not tasks:
        print("No tasks yet !")
    else:
        print("\nYour tasks: ")
        for index , task in enumerate(tasks):
            print(f"{index + 1}. {tasks}")

def task_mannager():
    tasks =[]
    while True:
        display_menu()
        choice = input("enter your choice(1-3): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_task(tasks)
        elif choice == '3':
            print("Exiting task manager. goodbye! ")
            break
        else:
            print("Invalid choice. Please enterr a number between 1 and 3 .")

if __name__ == "__main__":
    task_mannager()
