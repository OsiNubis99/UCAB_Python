from prettytable import PrettyTable

def generate_age_group_histogram(participants):
    # Counters for each age group
    juniors = 0
    seniors = 0
    masters = 0
    # Count participants by age group
    for participant in participants:
        age = participant.age
        if age <= 25:
            juniors += 1
        elif 26 <= age <= 40:
            seniors += 1
        else:
            masters += 1

    # Calculate percentage of participants in each age group
    total_participants = len(participants)
    juniors_percentage = juniors / total_participants * 100
    seniors_percentage = seniors / total_participants * 100
    masters_percentage = masters / total_participants * 100

    # Print histogram
    print("Histogram of participants by age group:")
    print("Juniors ({}): | {}".format(round(juniors_percentage), "*" * int(juniors_percentage / 10)))
    print("Seniors ({}): | {}".format(round(seniors_percentage), "*" * int(seniors_percentage / 10)))
    print("Masters ({}): | {}".format(round(masters_percentage), "*" * int(masters_percentage / 10)))

def print_table(participants):
    table = PrettyTable()
    if len(participants) == 0:
        return False
    # Get the properties of the Participant object (except hours, minutes, and seconds)
    properties = [prop for prop in vars(participants[0]).keys() if prop not in ['hours', 'minutes', 'seconds']]

    # Add columns to the table
    table.field_names = ["N°"] + properties + ["Time"]

    # Add participant data to the table
    for i, participant in enumerate(participants):
        row = [i + 1]
        row.extend(getattr(participant, prop) for prop in properties)
        time = f"{participant.hours}:{participant.minutes}:{participant.seconds}"
        row.append(time)
        table.add_row(row)

    # Print the table
    print(table)

def print_raw_table(objects):
    table = PrettyTable()
    if len(objects) == 0:
        return False
    # Get the properties of the Participant object (except hours, minutes, and seconds)
    properties = objects.keys()

    # Add columns to the table
    table.field_names = properties

    table.add_row(objects.values())

    # Print the table
    print(table)
