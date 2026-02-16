from utils import calculate_average, performance_assessment, calculate_average_all_students, get_student_info, \
    add_new_student, delete_student

def main(all_students, new_student):
    worst_student = None
    worst_grades = 100

    # Принт всех студентов
    print('Все студенты:')
    for student in all_students:
        # Вычисление среднего балла студента
        average_grade = calculate_average(student["grades"])
        # Оценка успешности студента
        performance = performance_assessment(average_grade)

        # Вычисление худшего студента
        if not average_grade:
            print(get_student_info(student['name'], avg_grade=0, performance=performance))
            continue
        elif average_grade < worst_grades:
            worst_grades = average_grade
            worst_student = student

        # Принт каждого студента
        print(get_student_info(student['name'], average_grade, performance))

    # Показ среднего балла всех студентов
    calculate_average_all_students(all_students)

    # Добавление нового студента и показ среднего балла всех студентов
    all_students = add_new_student(new_student, all_students)
    calculate_average_all_students(all_students)

    # Удаление худшего студента и показ среднего балла всех студентов
    all_students = delete_student(worst_student, all_students)
    calculate_average_all_students(all_students)

if __name__ == '__main__':
    students = [
        {'name': 'Harry', 'grades': [80, 90, 78]},
        {'name': 'Hermione', 'grades': [95, 90, 97]},
        {'name': 'Ron', 'grades': [60, 70, 64]},
        {'name': 'Draco', 'grades': [60, 75, 70]}
    ]

    student_to_list = {'name': 'Jinny', 'grades': []}

    main(students, student_to_list)