from classes.participant import Participant
from processing.functions import *

class Competition:
    def __init__(self):
        self.participants = []

    def load_participants_from_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) != 10:
                        raise ValueError("Error en archivo.")
                    ci, last_name1, last_name2, first_name, initial, gender, age, hours, minutes, seconds = data
                    participant = Participant(int(ci), last_name1.strip(), last_name2.strip(), first_name.strip(), initial.strip(), gender.strip(), int(age),
                                                int(hours), int(minutes), int(seconds))
                    self.participants.append(participant)

        except ValueError as error:
            raise ValueError(str(error))

    def list_participants(self):
        print_table(self.participants)

    def get_total_participants(self):
        total = len(self.participants)
        print(f"Participantes totales: {total}")

    def get_participants_by_age_group(self):
        age_groups = {
            'Juniors': lambda x: x <= 25,
            'Seniors': lambda x: 25 < x <= 40,
            'Masters': lambda x: x > 40
        }

        participants_by_group = {}
        for group, condition in age_groups.items():
            participants_by_group[group] = sum(1 for participant in self.participants if condition(participant.age))

        print_raw_table(participants_by_group)

    def get_participants_by_gender(self):
        participants_by_gender = {}
        for participant in self.participants:
            if participant.gender in participants_by_gender:
                participants_by_gender[participant.gender] += 1
            else:
                participants_by_gender[participant.gender] = 1
        print("Total femenino: ", str(participants_by_gender['F']), " y total masculino: ", str(participants_by_gender['M']))

    def get_winners_by_age_group(self):
        j = self.get_winner([participant for participant in self.participants if (participant.age <= 25)])
        s = self.get_winner([participant for participant in self.participants if (26 <= participant.age <= 40)])
        m = self.get_winner([participant for participant in self.participants if (41 <= participant.age)])
        return j+s+m

    def get_winners_by_gender(self):
        m = self.get_winner([participant for participant in self.participants if participant.gender == 'M'])
        f = self.get_winner([participant for participant in self.participants if participant.gender == 'F'])
        return m+f

    def get_winners_by_age_group_F(self):
        j = self.get_winner([participant for participant in [participant for participant in self.participants if participant.gender == 'F'] if (participant.age <= 25)])
        s = self.get_winner([participant for participant in [participant for participant in self.participants if participant.gender == 'F'] if (26 <= participant.age <= 40)])
        m = self.get_winner([participant for participant in [participant for participant in self.participants if participant.gender == 'F'] if (41 <= participant.age)])
        return j+s+m

    def get_winners_by_age_group_M(self):
        j = self.get_winner([participant for participant in [participant for participant in self.participants if participant.gender == 'M'] if (participant.age <= 25)])
        s = self.get_winner([participant for participant in [participant for participant in self.participants if participant.gender == 'M'] if (26 <= participant.age <= 40)])
        m = self.get_winner([participant for participant in [participant for participant in self.participants if participant.gender == 'M'] if (41 <= participant.age)])
        return j+s+m

    def get_winner(self, participants):
        return [ min(participants, key=lambda x: x.hours * 3600 + x.minutes * 60 + x.seconds) ]
