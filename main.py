class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def midle_grade(self):
        mg = sum(self.grades) / len(self.grades)
        return mg

    def __str__(self):
        name = f'Имя: {self.name}'
        sure_name = f'Фамилия: {self.surname}'
        md = "%.1f" % self.midle_grade()
        cor = f'Курсы в процессе изучения: {self.courses_in_progress}'
        corEND = f'Завершённые курсы: {self.finished_courses}'
        print(f'{name}')
        print(f'{sure_name}')
        print((f'Средняя оценка за доманшнее задание:{md}'))
        print(f'{cor}')
        return f'{corEND}'

    def garde_Lecturer(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def comparison(self):
        if (self.midle_grade()) > (Lecturer.midle_grade(some_lecturer) / 2):
            return ('Ученик учится лучше чем лектор ведёт лекции')
        elif (self.midle_grade()) == (Lecturer.midle_grade(some_lecturer) / 2):
            return ('Лектор ведет лекции примерно одинаково  с оценками учеников')
        else:
            return ('Ученик учится хуже чем лектор ведёт лекции')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __int__(self, grades):
        self.grades = {}

    def midle_grade(self):
        mg = sum(self.grades) / len(self.grades)
        return mg

    def __str__(self):
        name = f'Имя: {self.name}'
        sure_name = f'Фамилия: {self.surname}'
        md = "%.1f" % self.midle_grade()
        print(f'{name}')
        print(f'{sure_name}')
        return f'Средняя оценка за лекции:{md}'

    def comparison(self):
        if (self.midle_grade() / 2) > Student.midle_grade(some_student):
            return ('Лектор ведёт лекции лучше чем ученики учатся')
        elif (self.midle_grade() / 2) == Student.midle_grade(some_student):
            return ('Лектор ведет лекции примерно одинаково  с оценками учеников')
        else:
            return ('Лектор ведёт лекции хуже чем студенты учатся:')

class Reviewer(Mentor):
    def garde_Student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name = f'Имя: {self.name}'
        sure_name = f'Фамилия: {self.surname}'
        print(f'{name}')
        return f'{sure_name}'


some_reviewer = Reviewer('Vlad', 'Orehocolowich')
print(some_reviewer)
print(' ')
some_lecturer = Lecturer('Oleg', 'Ivanov')
some_lecturer.grades = 10, 10, 10, 9, 9, 10
print(some_lecturer)
print(' ')
some_student = Student('Jakob', 'Pshewalovic', 'M')
some_student.finished_courses = ','.join(['Програмирование введение'])
some_student.courses_in_progress = ','.join(['Курс Python разаботчика', 'Git'])
some_student.grades = [2, 5, 4, 3, 5, 5]
print(some_student)
print(' ')
print(Lecturer.comparison(some_lecturer))
print(' ')
print(Student.comparison(some_student))
print(' ')

alex = Student('Alex', 'Yorshina', 'W')
alex.finished_courses = ','.join(['Програмирование введение'])
alex.courses_in_progress = ['Курс Python разаботчика','Git']
alex.grades = [4,5,5,5,3,5]

steve = Student('Steve', 'Melsher', 'M')
steve.finished_courses = ['Програмирование введение']
steve.courses_in_progress = ['Курс Python разаботчика','Git']
steve.grades = [5,5,5,5,5,5]

bob = Lecturer('Bob', 'Shishkin')
bob.courses_attached = ['Програмирование введение','Курс Python разаботчика']
bob.grades = [10,10,10,10,9,10]

maria = Lecturer('Maria', 'Mercer')
maria.courses_attached = ['Git']
maria.grades = [8,9,8,8,10,7]

wroclav = Reviewer('Wroclav', 'Lion')
wroclav.courses_attached = ['Курс Python разаботчика']

jan = Reviewer('Jan', 'Sliznev')
jan.courses_attached = ['Git']

student_list = [alex.__dict__,steve.__dict__]
gr = 0
operation = 0
check_cor = input('Введите название курса:')
gr_cour = 0

for check in student_list:
    for one, two in check.items():
        if one == 'courses_in_progress':
            operation += 1
            if check_cor in two:
                for one, two in check.items():
                    if one == 'grades':
                        gr_cour += sum(two)
                        gr += len(two)
                        if operation == len(student_list):
                            enter = "%.1f" % (gr_cour / gr)
                            print(f'Средний оценка Студентов за курс {check_cor} равняется {enter}.')
                            break
            elif operation == len(student_list):
                enter = "%.1f" % (gr_cour / gr)
                print(f'Средний оценка Студентов за курс {check_cor} равняется {enter}.')
                break

lecturer_list = [maria.__dict__,bob.__dict__]
check_cor_two = input('Введите название курса:')
gr = 0
operation = 0
gr_cour = 0

for check in lecturer_list:
    for one, two in check.items():
        if one == 'courses_attached':
            operation += 1
            if check_cor_two in two:
                    for one, two in check.items():
                        if one == 'grades':
                            gr_cour += sum(two)
                            gr += len(two)
                            if operation == len(lecturer_list):
                                enter = "%.1f" % (gr_cour / gr)
                                print(f'Средний оценка Лекторов за курс {check_cor} равняется {enter}.')
                                break
            elif operation == len(lecturer_list):
                enter = "%.1f" % (gr_cour / gr)
                print(f'Средний оценка Лекторов за курс {check_cor} равняется {enter}.')
                break

