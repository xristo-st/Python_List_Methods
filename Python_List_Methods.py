import random
from blessed import Terminal

term = Terminal()

CREATE  = "1"
APPEND  = "2"
EXTEND  = "3"
INSERT  = "4"
REMOVE  = "5"
POP     = "6"
CLEAR   = "7"
INDEX   = "8"
COUNT   = "9"
SORT    = "10"
REVERSE = "11"
COPY    = "12"
EXIT    = "e"
menu_items = { CREATE: " create list",
               APPEND: " append()",
               EXTEND: " extend()",
               INSERT: " insert()",
               REMOVE: " remove()",
               POP: " pop()",
               CLEAR: " clear()",
               INDEX: " index()",
               COUNT: " count()",
               SORT: "sort()",
               REVERSE: "reverse()",
               COPY: "copy()",
               EXIT: " exit"
             }

RANDOM_INT = '1'
RANDOM_FLOAT = '2'
RANDOM_STRING = '3'
RANDOM_BOOL = '4'
RANDOM_MIXED = '5'
INPUT_LIST = '6'
create_menu = { RANDOM_INT: "random integers",
                RANDOM_FLOAT: "random float",
                RANDOM_STRING: "random string",
                RANDOM_BOOL: "random boolean",
                RANDOM_MIXED: "random mixed",
                INPUT_LIST: "input list"
               }


def list_separation(text: str) -> list:
    text = text.replace(', ', ',')
    result = text.split(',')
    for i in range(len(result)):
        result[i] = guess_the_type(result[i])
    return result


def press_key_to_continue():
    print("\nPress a key to continue...")
    with term.cbreak():
        key = term.inkey()
        print(term.normal)


def guess_the_type(item: str):
    if item == 'None':
        return None
    if item == "True":
        return True
    if item == "False":
        return False
    if len(item) > 1:
        if (item[0] == '"' and item[-1] == '"') or \
            (item[0] == "'" and item[-1] == "'"):
            return item[1:-1]
    try:
        item = int(item)
        return item
    except ValueError:
        pass
    try:
        item = float(item)
        return item
    except ValueError:
        pass
    return item


def random_str() -> str:
    length = random.randint(1,5)
    result = ""
    for i in range(length):
        result += chr(random.randint(65, 122))
    return result


def random_int_list(length: int) -> list[int]:
    return [random.randint(-100, 100) for _ in range(length)]


def random_float_list(length: int) -> list[float]:
    return [random.randint(-1000, 1000) / 10 for _ in range(length)]


def random_str_list(length: int) -> list[str]:
    return [random_str() for _ in range(length)]


def random_bool_list(length: int) -> list[bool]:
    return [bool(random.randint(0, 1)) for _ in range(length)]


def random_mixed_list(length: int) -> list:
    result = []
    for _ in range(length):
        item = None
        random_type = str(random.randint(1, 5))
        if random_type == RANDOM_INT:
            item = random.randint(-100, 100)
        elif random_type == RANDOM_FLOAT:
            item = random.randint(-1000, 1000) / 10
        elif random_type == RANDOM_STRING:
            item = random_str()
        elif random_type == RANDOM_BOOL:
            item =  bool(random.randint(0,1))
        elif random_type == 5:
            item = None
        result.append(item)
    return result


def create_list() -> list:
    # print(term.home + term.move_xy(0, 2) + term.clear_eos, end="")
    print(term.underline_bright_red + "\nCREATE LIST\n" + term.normal)
    result = []
    for item in create_menu:
        print(f"({item}) {create_menu[item]}")
    command = input("Choose: ")
    if command not in create_menu:
        print("Incorrect command")
    elif command == INPUT_LIST:
        print("Enter a list (separated by commas): ")
        result = list_separation(input())
    else:
        length = random.randint(1, 10)
        if command == RANDOM_INT:
            result = random_int_list(length)
        elif command == RANDOM_FLOAT:
            result = random_float_list(length)
        elif command == RANDOM_STRING:
            result = random_str_list(length)
        elif command == RANDOM_BOOL:
            result = random_bool_list(length)
        else:
            result = random_mixed_list(length)
    return result


def insert_method(lst: list):
    print(term.underline_bright_red + "\nMethod insert()\n" + term.normal)
    print("insert() method have 2 arguments: index and new element.")
    print("Index can be any integer number and new element can be anything.\n")
    while True:
        idx = input("Index, where the new element to be inserted: ")
        try:
            idx = int(idx)
            break
        except ValueError:
            print("Wrong input")
    item = guess_the_type(input("New element: "))
    print(f"\nBefore: {lst}")
    lst.insert(idx, item)
    print(f"After:  {lst}")
    press_key_to_continue()


def append_method(lst: list):
    print(term.underline_bright_red + "\nMethod append()\n" + term.normal)
    print("The method accept 1 argument, which can be of any type.")
    print("It will be added at the end of the list\n")
    new_item = guess_the_type(input("New element: "))
    print(f"\nBefore: {lst}")
    lst.append(new_item)
    print(f"After:  {lst}")
    press_key_to_continue()


def extend_method(lst: list):
    # print(term.home + term.move_xy(0, 2) + term.clear_eos, end="")
    print(term.underline_bright_red + "\nMethod extend()\n" + term.normal)
    print("The method accept 1 argument, which can be an iterable object")
    print("The elements of this object will be added at the end of the list\n")
    print("Enter new list (separated by commas): ")
    new_list = list_separation(input())
    print(f"Before: {lst}")
    lst.extend(new_list)
    print(f"After:  {lst}")
    press_key_to_continue()


def remove_method(lst: list):
    print(term.underline_bright_red + "\nMethod remove()\n" + term.normal)
    print("remove() method have 1 argument: the element to be removed.")
    print("The element can be any type. If the element is not in the list,")
    print("the program will raise the exception 'ValueError'\n")
    item = guess_the_type(input("Element to be removed: "))
    if item not in lst:
        print("The element is not in the list")
    else:
        print(f"Before: {lst}")
        lst.remove(item)
        print(f"After:  {lst}")
    press_key_to_continue()


def pop_method(lst: list):
    print(term.underline_bright_red + "\nMethod pop()\n" + term.normal)
    print("pop() method have 1 argument: the index of the element to be popped out")
    print("If the index is omitted then the last element of the list will be popped out.\n")
    while True:
        idx = input("Index: ")
        if idx == '':
            break
        else:
            try:
                idx = int(idx)
                if -len(lst) <= idx < len(lst):
                    break
                else:
                    print("Index out of range")
            except ValueError:
                print("Wrong input")
    print(f"Before: {lst}")
    if idx == '':
        popped_out = lst.pop()
    else:
        popped_out = lst.pop(idx)
    print(f"After:  {lst}")
    print(f"The return value of pop({idx}) = {popped_out}")
    press_key_to_continue()


def clear_method(lst: list):
    print(term.underline_bright_red + "\nMethod clear()\n" + term.normal)
    print("clear() method have no argument.")
    print("It removes all the elements of the list.\n")
    print(f"Before: {lst}")
    lst.clear()
    print(f"After:  {lst}")
    press_key_to_continue()


def index_method(lst: list):
    print(term.underline_bright_red + "\nMethod index()\n" + term.normal)
    print("index() method have 1 argument: an element from the list.")
    print("If the element is in the list,it will return the index")
    print("of first instance of that element in the list.")
    print("Else the program will raise the exception 'ValueError'\n")
    item = guess_the_type(input("Element: "))
    if item not in lst:
        print("The element is not in the list")
    else:
        idx = lst.index(item)
        print(f"The index of {item} is: {idx}")
    press_key_to_continue()


def count_method(lst: list):
    print(term.underline_bright_red + "\nMethod count()\n" + term.normal)
    print("count() method have 1 argument: an element from the list.")
    print("The method will return how many times the element is in the list\n")
    item = guess_the_type(input("Element: "))
    count = lst.count(item)
    print(f"Element {item} have {count} instances in the list.")
    press_key_to_continue()


def sort_method(lst: list):
    print(term.underline_bright_red + "\nMethod sort()\n" + term.normal)
    print("sort() method have 2 arguments, 'key' and 'reverse'")
    print("if reverse is not used, the elements will be sort in ascending order")
    print("if 'reverse=True' is used, the elements will be sort in descending order")
    print("All elements must be of same type, else the program will raise 'TypeError' exception\n")
    try:
        print(f"Before: {lst}")
        lst.sort()
        print(f"After:  {lst}")
    except TypeError:
        print("The list cannot be sorted")
    press_key_to_continue()


def reverse_method(lst: list):
    print(term.underline_bright_red + "\nMethod reverse()\n" + term.normal)
    print("reverse() method have no arguments")
    print("It reverse the order of the elements\n")
    print(f"Before: {lst}")
    lst.reverse()
    print(f"After:  {lst}")
    press_key_to_continue()


def copy_method(lst: list):
    print(term.underline_bright_red + "\nMethod copy()\n" + term.normal)
    print("copy() method have no arguments")
    print("It returns a copy of the list\n")
    print(f"Your list: {lst}")
    copy_of_lst = lst.copy()
    print(f"Copy of your list:  {lst}")
    press_key_to_continue()

def main():
    print(term.home + term.clear + "Pyton list methods: exercise", end="")
    print()
    lst = []
    while True:
        print(term.home + term.move_xy(0, 2) + term.clear_eos, end="")
        print(term.bright_cyan + f"Your list: {lst}\n" + term.normal)
        for item in menu_items:
            print(f"({item}) {menu_items[item]}")
        command = input("\nChoose a method: ").lower()
        if command == EXIT:
            break
        if command not in menu_items:
            print("Incorrect choice")
            press_key_to_continue()
            continue
        if command == CREATE:
            lst = create_list()
        elif command == APPEND:
            append_method(lst)
        elif command == EXTEND:
            extend_method(lst)
        elif command == INSERT:
            insert_method(lst)
        elif command == REMOVE:
            remove_method(lst)
        elif command == POP:
            pop_method(lst)
        elif command == CLEAR:
            clear_method(lst)
        elif command == INDEX:
            index_method(lst)
        elif command == COUNT:
            count_method(lst)
        elif command == SORT:
            sort_method(lst)
        elif command == REVERSE:
            reverse_method(lst)
        elif command == COPY:
            copy_method(lst)


if __name__ == "__main__":
    main()