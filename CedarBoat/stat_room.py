from paths import data_path

import linecache

import start_paper_amount_calc

global total_paper_amount_width, total_paper_amount_length
global paper_amount_length, paper_amount_width, paper_amount_sides
global first_person_weight, second_person_weight

def refresh_values():
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

    start_stat_room()

def start_stat_room():
    if paper_amount_length == 0 or paper_amount_width == 0:
        print("\n-----------------------------------------------")
        print("Cannot load page without boats length and width")
        print("-----------------------------------------------\n")
        return_to_main_menu()
    else:
        if total_paper_amount_length == 0:
            print("\n!Missing Value! = total_paper_amount_length")
        if total_paper_amount_width == 0:
            print("\n!Missing Value! = total_paper_amount_width")
        if paper_amount_sides == 0:
            print("\n!Missing Value! = paper_amount_sides")
        if first_person_weight == 0:
            print("\n!Missing Value! = first_person_weight")
        if second_person_weight == 0:
            print("\n!Missing Value! = second_person_weight")

        answer = input(f"\nStat Room\n"
              f"Total Paper Dimensions: {total_paper_amount_length}L x {total_paper_amount_width}W\n"
              f"Your Boats Dimensions: {paper_amount_length}L x {paper_amount_width}W x {paper_amount_sides}H\n"
              f"\n"
              f"REMAINING PAPER: {(total_paper_amount_length * total_paper_amount_width) - (paper_amount_length * (paper_amount_width + (paper_amount_sides * 2)))} Square Inches"
              f"\n"
              f"Boats Max Capacity: {round((paper_amount_length * paper_amount_width * paper_amount_sides) * 0.03611, 2)} Pounds\n"
              f"Weight Inside Boat: Front - {first_person_weight} Pounds, Back - {second_person_weight} Pounds, Total (Paddles, LifeJackets, Paper) - {first_person_weight + second_person_weight + 16} Pounds\n"
              f"\n"
              f"Sidewall Minimum (Amount Under Water): {round((first_person_weight + second_person_weight + 16) / (paper_amount_length * paper_amount_width * 0.03611), 2)} Inches\n"         
              f"Freeboard: {round(paper_amount_sides - (first_person_weight + second_person_weight + 16) / (paper_amount_length * paper_amount_width * 0.03611), 2)} Inches\n"
              f"\n"
              f"Press enter to return\n")
        if answer == "".strip().lower():
            return_to_main_menu()

def return_to_main_menu():
    from main import main_menu

    main_menu()