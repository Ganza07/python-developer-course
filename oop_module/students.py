class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

if __name__ == "__main__":
    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')
    print(isinstance(lecturer, Mentor)) # True
    print(isinstance(reviewer, Mentor)) # True
    print(lecturer.courses_attached)    # []
    print(reviewer.courses_attached)    # []