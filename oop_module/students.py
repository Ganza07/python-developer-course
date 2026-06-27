class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_grade(self):
        all_grades = [g for grades in self.grades.values() for g in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade():.1f}"

    def __eq__(self, other):
        return isinstance(other, Lecturer) and self._average_grade() == other._average_grade()

    def __lt__(self, other):
        return isinstance(other, Lecturer) and self._average_grade() < other._average_grade()

    def __gt__(self, other):
        return isinstance(other, Lecturer) and self._average_grade() > other._average_grade()

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _average_grade(self):
        all_grades = [g for grades in self.grades.values() for g in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        courses = ", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет"
        finished = ", ".join(self.finished_courses) if self.finished_courses else "Нет"
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self._average_grade():.1f}\n"
                f"Курсы в процессе изучения: {courses}\n"
                f"Завершенные курсы: {finished}")

    def __eq__(self, other):
        return isinstance(other, Student) and self._average_grade() == other._average_grade()

    def __lt__(self, other):
        return isinstance(other, Student) and self._average_grade() < other._average_grade()

    def __gt__(self, other):
        return isinstance(other, Student) and self._average_grade() > other._average_grade()

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


# Тестирование Задания №2
if __name__ == "__main__":
    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')
    student = Student('Ольга', 'Алёхина', 'Ж')

    student.courses_in_progress += ['Python', 'Java']
    lecturer.courses_attached += ['Python', 'C++']
    reviewer.courses_attached += ['Python', 'C++']
    print("\n=== Тест Задания 2 ===")
    print(student.rate_lecture(lecturer, 'Python', 7))  # None
    print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
    print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
    print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

    print(lecturer.grades)  # {'Python': [7]}

    print("\n=== Тест Задания 3 ===")
    print(reviewer)
    print(lecturer)
    print(student)

    # Проверка сравнения
    lecturer2 = Lecturer('Мария', 'Смирнова')
    lecturer2.courses_attached += ['Python']
    student.rate_lecture(lecturer2, 'Python', 8)
    print(f"\nСравнение лекторов: {lecturer > lecturer2}")  # True или False в зависимости от оценок
