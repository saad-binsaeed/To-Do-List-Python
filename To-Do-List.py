tasks=[]
def add():
    user_task=input('enter your Task')
    tasks.append(user_task)
    print('Task Added Successfully')

def remove():
    try:
        rmv=int(input('enter task number you want to remove'))
        print('\n Current tasks : ')

        for i, task in enumerate(tasks , start=1):
            print(i , tasks[i])    

        if 1>= rmv <= len(tasks):
            removed=tasks.pop(rmv)
            print(f'{removed} is Removed succecssfully')
        else:
            print("invalid input")

    except ValueError:
        print('You entered an invalid value')

def show():
    if not tasks:
        print('YOur List is empty')
    else:
        print('Your taks are :')
        for i, task in enumerate(tasks):
            print(i+1, tasks[i])

while True:
    print('-----------TO DO LIST------------')
    print('1. Add a Task')            
    print('2. Remove a Task')            
    print('3. Show the Tasks') 
    print('4. Exit')

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add()

    elif choice == "2":
        remove()

    elif choice == "3":
        show()

    elif choice == "4":
        print("Thank you for using the To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")