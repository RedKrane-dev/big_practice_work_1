from utils import calculate_average, performance_assessment, calculate_average_all_students
# 1
students = [
    {'name': 'Harry', 'grades': [80, 90, 78]},
    {'name': 'Hermione', 'grades': [95, 90, 97]},
    {'name': 'Ron', 'grades': [60, 70, 64]},
    {'name': 'Draco', 'grades': [60, 75, 70]}
]

def main(all_students, new_student):
    worst_student = None
    worst_grades = 100

    # 4
    print('Все студенты:')
    for student in all_students:
        average_grade = calculate_average(student["grades"])

        if average_grade < worst_grades:
            worst_grades = average_grade
            worst_student = student

        print(
            f'Студент: {student["name"]}\n'
            f'Средний балл: {average_grade}\n'
            f'Статус: {performance_assessment(average_grade)}\n'
        )

    # 5
    print(
        f'Средний балл всех студентов:\n'
        f'{calculate_average_all_students(all_students)}\n'
    )

    # 6
    all_students.append(new_student)
    print(
        f'Добавлен новый студент - {new_student["name"]}\n'
        f'Средний балл всех студентов:\n'
        f'{calculate_average_all_students(all_students)}\n'
    )
    # 6
    all_students.remove(worst_student)
    print(
        f'Удален худший студент - {worst_student["name"]}\n'
        f'Средний балл всех студентов:\n'
        f'{calculate_average_all_students(all_students)}\n'
    )

if __name__ == '__main__':
    student_to_list = {'name': 'Jinny', 'grades': [89, 88, 90]}
    main(students, student_to_list)