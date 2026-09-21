from paths import data_path

import linecache

global total_paper_amount_width, total_paper_amount_length
global paper_amount_length, paper_amount_width, paper_amount_sides
global first_person_weight, second_person_weight

# Hola if you're here in the code, the most important thing here is the file saving function
# To save info to the file, you must run "save_info_to_file" with the integrated settings (line_number, new_info)
#
# The file is structured as below:
# 1st = total_paper_amount_length
# 2nd = total_paper_amount_width
# 3rd = paper_amount_length
# 4th = paper_amount_width
# 5th = paper_amount_sides
# 6th = first_person_weight
# 7th = second_person_weight


def new_input_question():
    global total_paper_amount_width, total_paper_amount_length
    global paper_amount_length, paper_amount_width, paper_amount_sides
    global first_person_weight, second_person_weight

    path = data_path()
    linecache.checkcache(path)

    total_paper_amount_length = float(linecache.getline(path, 1))
    total_paper_amount_width = float(linecache.getline(path, 2))
    paper_amount_length = float(linecache.getline(path, 3))
    paper_amount_width = float(linecache.getline(path, 4))
    paper_amount_sides = float(linecache.getline(path, 5))
    first_person_weight = float(linecache.getline(path, 6))
    second_person_weight = float(linecache.getline(path, 7))

    while True:
        answer = input("What information would you like to change?\n"
                       "1 --- Total Paper Dimensions\n"
                       "2 --- Your Boats Dimensions\n"
                       "3 --- Your Weight Inside Boat\n"
                       "\n"
                       "Press Enter to return to the main menu")
        if answer == "1".strip().lower():
            total_paper_amount_ask()
            break
        elif answer == "2".strip().lower():
            paper_amount_ask()
            break
        elif answer == "3".strip().lower():
            weight_inside_boat()
            break
        else:
            from main import main_menu
            main_menu()

def total_paper_amount_ask():
    global total_paper_amount_width, total_paper_amount_length

    total_paper_amount_length = float(input("What is the total length (inches) rolled out of paper?"))
    total_paper_amount_width = float(input("What is the total width (inches) rolled out of paper?"))
    save_info_to_file(1, total_paper_amount_length)
    save_info_to_file(2, total_paper_amount_width)
    new_input_question()

def paper_amount_ask():
    global total_paper_amount_width, total_paper_amount_length
    global paper_amount_length, paper_amount_width, paper_amount_sides

    paper_amount_length = float(input("How long (inches) would you like your boat to be?"))
    paper_amount_width = float(input("How wide (inches) would you like your boat to be? (Do not include height of sides)"))

    while True:
        if paper_amount_width >= total_paper_amount_width:
            print(f"{total_paper_amount_width}")
            print("The paper is not wide enough")
            paper_amount_ask()
        if paper_amount_length > total_paper_amount_length:
            print("The paper is not long enough")
            paper_amount_ask()
        else:
            paper_amount_sides = float((total_paper_amount_width - paper_amount_width) / 2)
            answer = input(f"With your desired width your side walls can maximum be {paper_amount_sides} tall (inch)\n"
                           f"Do you wish to keep this height? (y/n)")
            if answer == "y".strip().lower():
                save_info_to_file(3, paper_amount_length)
                save_info_to_file(4, paper_amount_width)
                save_info_to_file(5, paper_amount_sides)
                new_input_question()
                break
            elif answer == "n".strip().lower():
                question = float(input("How tall (inches) would you like your side walls to be (individually)"))
                if question > paper_amount_sides:
                    print("You don't have enough paper to make sidewalls that tall")
                    print(f"Your boat's width would have to be {total_paper_amount_width - (question * 2)} wide")
                    answer = input("Would you like to change your boats width? (y/n)")
                    if answer == "y".strip().lower():
                        paper_amount_ask()
                    elif answer == "n".strip().lower():
                        break
                elif question <= paper_amount_sides:
                    paper_amount_sides = question
                    print(f"Sides will be {paper_amount_sides} tall")
                    save_info_to_file(3, paper_amount_length)
                    save_info_to_file(4, paper_amount_width)
                    save_info_to_file(5, paper_amount_sides)
                    new_input_question()
                    break
                else:
                    print("Something went wrong")
            else:
                paper_amount_ask()

def weight_inside_boat():
    global first_person_weight, second_person_weight

    first_person_weight = float(input("How much does the first person weigh? (pounds)"))
    second_person_weight = float(input("How much does the second person weigh? (pounds)"))
    save_info_to_file(6, first_person_weight)
    save_info_to_file(7, second_person_weight)
    new_input_question()

def save_info_to_file(line_number, new_value):
    from paths import data_path

    with open(data_path(), "r") as f:
        lines = f.readlines()

        lines[line_number - 1] = str(new_value) + "\n"

    with open(data_path(), "w") as f:
        f.writelines(lines)