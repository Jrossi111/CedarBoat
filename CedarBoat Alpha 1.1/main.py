import time
import sys

from start_paper_amount_calc import new_input_question
from stat_room import refresh_values

def main_menu():
    while True:
        print("\n" * 100)
        print("CedarBoat Alpha 1.1\n")
        print("1 --- Input New Information\n"
              "2 --- Frame Builder (In Development)\n"
              "3 --- Recommendations (In Development)\n"
              "\n"
              "stat --- Statistics of your Boat\n"
              "about --- Shows Further Information\n"
              "credit --- Shows the Awesome People who made this\n"
              "\n"
              "exit --- exit :/\n")

        answer = input("Choose an option:").strip().lower()
        if answer == "1".strip():
            new_input_question()
            break
        elif answer == "2":
            print("\n" * 100)
            print("In development")
            time.sleep(2)
        elif answer == "3":
            print("\n" * 100)
            print("In development")
            time.sleep(2)
        elif answer == "stat":
            refresh_values()
            break
        elif answer == "exit":
            exit_function()
            break
        elif answer == "about":
            print("\n" * 100)
            input("Hola, My name is Javan Rossignol and I am a Cyber Operations major at Cedarville University\n"
                  "I was heavily inspired to make this project when I was told that I would have to participate in the paper canoe race for engineering students.\n"
                  "Personally, I believe I shouldn't have to take a course that has nothing to do with my major\n"
                  "\n"
                  'My goal with this project is to create a hypothetical "perfect" solution for your race\n'
                  'During my time making my boat we were recommended to use AI to make us calculators and other information tools\n'
                  "I think that's lazy and dumb, and honestly they never worked, so here we are\n"
                  "\n"
                  "I hope this tool makes the boat race super easy for you, and to replace AI from failing at it's job\n"
                  "\n"
                  "Press enter to return to the main menu")
        elif answer == "credit":
            print("\n" * 100)
            input("Javan Rossignol - Head Programmer\n"
                  "Caleb Lilly - Concept Development, Bug Testing\n"
                  "Samuel Parlette - Mathematician, Bug Testing\n"
                  "Logan Weaver - Mathematician\n"
                  "\n"
                  "Press enter to return to the main menu")
        else:
            print("Invalid option")

def exit_function():
    sys.exit(0)

main_menu()