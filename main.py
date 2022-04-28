class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}        
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def avg_grades(self):
        for self.avg_grades_main in self.grades.values():
            self.avg_grades_main = round(sum(self.avg_grades_main)/len(self.avg_grades_main), 1)
            return self.avg_grades_main
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студенты')
            return
        return self.avg_student_grades < other.avg_student_grades
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание:{self.avg_grades_main} \nКурсы в процессе изучения:{self.courses_in_progress} \nЗавершенные курсы{self.finished_courses}'      
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []              
class Lecturer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def avg_grades(self):
        for self.avg_grades_main in self.grades.values():
            self.avg_grades_main = round(sum(self.avg_grades_main)/len(self.avg_grades_main), 1)
            return self.avg_grades_main
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции:{self.avg_grades_main}'
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лекторы')
            return
        return self.avg_grades_main < other.avg_grades_main
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'
 
student_vlad = Student('Владислав', 'Пырков', 'мужской')
student_vlad.finished_courses = ['Введение в программирование']
student_vlad.courses_in_progress += ['Python', 'Git']
student_kira = Student('Кира', 'Васильева', 'женский')
student_kira.finished_courses = ['Введение в программирование']
student_kira.courses_in_progress += ['Python', 'Git']

mentor_oleg = Lecturer('Олег', 'Петров')
mentor_oleg.courses_attached += ['Python']
mentor_vasiliy = Lecturer('Василий', 'Пупков')
mentor_vasiliy.courses_attached += ['Git']

reviewer_olga = Reviewer('Ольга', 'Андреева')
reviewer_olga.courses_attached += ['Python', 'Git']
reviewer_olga.rate_hw(student_vlad, 'Python', 10)
reviewer_olga.rate_hw(student_vlad, 'Python', 10)
reviewer_olga.rate_hw(student_vlad, 'Git', 6)
reviewer_olga.rate_hw(student_vlad, 'Git', 10)
reviewer_olga.rate_hw(student_kira, 'Python', 10)
reviewer_olga.rate_hw(student_kira, 'Python', 9)
reviewer_olga.rate_hw(student_kira, 'Git', 7)
reviewer_olga.rate_hw(student_kira, 'Git', 8)
list_1 = [student_vlad.grades, student_kira.grades]

student_vlad.rate_hw(mentor_oleg, 'Python', 10)
student_vlad.rate_hw(mentor_oleg, 'Python', 10)
student_vlad.rate_hw(mentor_vasiliy, 'Git', 5)
student_vlad.rate_hw(mentor_vasiliy, 'Git', 7)
student_kira.rate_hw(mentor_oleg, 'Python', 10)
student_kira.rate_hw(mentor_oleg, 'Python', 10)
student_kira.rate_hw(mentor_vasiliy, 'Git', 9)
student_kira.rate_hw(mentor_vasiliy, 'Git', 8)
list_2 = [mentor_oleg.grades, mentor_vasiliy.grades]

student_vlad.avg_grades()
student_kira.avg_grades()
mentor_oleg.avg_grades()
mentor_vasiliy.avg_grades()

def avg_grades(list):
    list2 = []
    for avg_grades_mains in list:
        for avg_grades_main in avg_grades_mains.values():
            for avg_grades in avg_grades_main:
                    while list2.append(avg_grades):
                        break
    list2 = round(sum(list2)/len(list2), 1)
    return list2

print('Студенты: ')
print()
print(student_vlad)
print()
print(student_kira)
print()
print(f'Средняя оценка всех студентов за все курсы: {avg_grades(list_1)}')
print('---------------')
print('Лекторы: ')
print()
print(mentor_oleg)
print()
print(mentor_vasiliy)
print()
print(f'Средняя оценка всех лекторов за все курсы: {avg_grades(list_2)}')
print('---------------')
print('Ревьюверы: ')
print()
print(reviewer_olga)
print()
print()























