from os import path

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global all_data, id
    with open(file_base, 'r', encoding='utf8') as f:
        all_data = [i.strip() for i in f]
        id = int(all_data[-1][0])
        return all_data


def show_all():
    if not all_data:
        print('Empty data')
    print(*all_data, sep="\n")


def add_new_contact():
    global id
    array = ['Surname', 'Name', 'Fathersname', 'Phone number']
    string = ''
    for i in array:
        string += input(f"Enter {i} ") + " "
    id += 1
    with open(file_base, 'a', encoding="utf-8") as f:
        f.write(f"{id} {string}\n")


def serch_contact():
    search = input("Serch: ")
    with open(file_base, 'r', encoding="utf-8") as f:
        for i in f:
            str = i.split()
            # print(str)
            for j in str:
                # print(j)
                if j == search:
                    print(i)


def change_contact():
    global all_data, id
    show_all()
    change = input("Enter the id of the record to be change: ")
    change_data = []
    id = int(change)
    string = ''
    array = ['Surname', 'Name', 'Fathersname', 'Phone number']
    string = ''
    for i in array:
        string += input(f"Enter new {i} ") + " "
    string = change + " " + string
    with open(file_base, 'r', encoding="utf-8") as f:   
        for i in f:
            str = i.split()
            print(str)
            if str[0] < change:
                change_data.append(i)
            elif str[0] == change:
                change_data.append(string)
            elif str[0] > change:
                change_data.append(i)
    # print (change_data)
    change_data = [i.strip() for i in change_data]
    # print (change_data)
    with open(file_base, 'w', encoding="utf-8") as f:
        for i in range(len(change_data)):
            f.write(f"{change_data[i]}\n")


def delete_contact():
    global all_data, id
    show_all()
    delete = input("Enter the id of the record to be deleted: ")
    new_data = []
    id = int(delete)
    with open(file_base, 'r', encoding="utf-8") as f:   
        for i in f:
            str = i.split()
            print(str)
            if str[0] != delete:
                if str[0] < delete:
                    new_data.append(i)
                elif str[0] > delete:
                    i = f"{id} {str[1]} {str[2]} {str[3]} {str[4]}\n"
                    id += 1
                    new_data.append(i)
    # print (new_data)
    new_data = [i.strip() for i in new_data]
    # print (new_data)
    with open(file_base, 'w', encoding="utf-8") as f:
        for i in range(len(new_data)):
            f.write(f"{new_data[i]}\n")
            # all_data = new_data
                

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change a record\n"
                       "5. Delete a record\n"
                       "6. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
                pass
            case "3":
                serch_contact()
                pass
            case "4":
                change_contact()
                pass
            case "5":
                delete_contact()
                pass
            case "6":
                play = False
            case _:
                print("Try again!\n")


main_menu()
