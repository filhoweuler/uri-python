
def print_list(lst):
    for it in lst:
        print(it)
def show_help():
    print("DONE - exit the program")
    print("SHOW - show your list")

todo = []
item = ""

while True:
    item = input("Enter an item to your to-do list: ")

    if item == 'DONE':
        break

    if item == 'SHOW':
        print_list(todo)
    elif item == 'HELP':
        show_help()
    else:        
        todo.append(item)
    

for it in todo:
    print(it)
