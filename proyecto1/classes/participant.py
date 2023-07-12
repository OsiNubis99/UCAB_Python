class Participant:
    def __init__(self, ci, last_name1, last_name2, first_name, initial, gender, age, hours, minutes, seconds):
        self._validate_ci(ci)
        self._validate_last_name(last_name1)
        self._validate_last_name(last_name2)
        self._validate_name(first_name)
        self._validate_initial(initial)
        self._validate_gender(gender)
        self._validate_age(age)
        self._validate_time(hours, minutes, seconds)

        self.ci = ci
        self.last_name1 = last_name1
        self.last_name2 = last_name2
        self.first_name = first_name
        self.initial = initial
        self.gender = gender
        self.age = age
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def _validate_ci(self, ci):
        if not 0 < ci:
            raise ValueError("El CI debe contener solo números.")

    def _validate_last_name(self, last_name):
        if not last_name.replace(" ", "").isalpha():
            raise ValueError("El last_name debe contener solo letras.", last_name)

    def _validate_name(self, first_name):
        if not first_name.replace(" ", "").isalpha():
            raise ValueError("El first_name debe contener solo letras.")

    def _validate_initial(self, initial):
        if not initial.isalpha() or len(initial) > 1:
            raise ValueError("La initial debe ser una única letra.")

    def _validate_gender(self, gender):
        if gender not in ['M', 'F']:
            raise ValueError("El gender debe ser 'M' o 'F'.")

    def _validate_age(self, age):
        if not (0 < age < 200):
            raise ValueError("La age debe ser un número mayor a 0 y menor a 200.")

    def _validate_time(self, hours, minutes, seconds):
        if not (0 <= hours < 24) or not (0 <= minutes < 60) or not (0 <= seconds < 60):
            raise ValueError("El tiempo debe ser una hora válida (formato: hh:mm:ss).")
