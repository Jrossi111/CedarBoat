import sys

from start_paper_amount_calc import new_input_question
from stat_room import refresh_values

def main_menu():
    while True:
        print("CedarBoat Alpha 1.0\n")
        print("1 --- Input New Information\n"
              "2 --- Frame Builder\n"
              "3 --- Recommendations\n"
              "\n"
              "stat --- Statistics of your Boat\n"
              "about --- Shows Further Information\n"
              "exit --- exit :/\n")

        answer = input("Choose an option:")
        if answer == "1".strip():
            new_input_question()
            break
        elif answer == "2":
            print("In development")
        elif answer == "3":
            print("In development")
        elif answer == "stat":
            refresh_values()
            break
        elif answer == "exit":
            close()
            break
        elif answer == "about":
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
        else:
            print("Invalid option")
            main_menu()

def close():
    quit()


main_menu()