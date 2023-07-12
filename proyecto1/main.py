# main.py
from processing.functions import generate_age_group_histogram, print_table
from views.actions_menu import show_actions_menu
from views.file_menu import show_file_menu
from views.main_menu import show_main_menu
from classes.competition import Competition

competition = Competition()
           
while True:
    print("-"*50)
    option = show_main_menu()
    print("-"*50)
    if option == '1':
        while True:
            file_option = show_file_menu()
            if file_option == '1':
                try:
                    participants = competition.load_participants_from_file("./file/competencia.txt")
                except ValueError as error:
                    print("Error: ", str(error))
            elif file_option == '2':
                break
    elif option == '2':
        while True:
            print("-"*50)
            action_option = show_actions_menu()
            print("-"*50)
            if action_option == '1':
                competition.list_participants()
            if action_option == '2':
                competition.get_total_participants()
            if action_option == '3':
                competition.get_participants_by_age_group()
            if action_option == '4':
                competition.get_participants_by_gender()
            if action_option == '5':
                print_table(competition.get_winners_by_age_group())
            if action_option == '6':
                print_table(competition.get_winners_by_gender())
            if action_option == '7':
                print_table(competition.get_winners_by_age_group_F())
                print()
                print_table(competition.get_winners_by_age_group_M())
            if action_option == '8':
                print_table(competition.get_winner(competition.participants))
            if action_option == '9':
                generate_age_group_histogram(competition.participants)
            if action_option == '10' or action_option == '0':
                break
    else: 
        break
