def calculate_average(grades: list[int]) -> float | None:
    """
    Принимает список оценок студента и возвращает среднее значение
    """
    try:
        result = sum(grades) / len(grades)
        return round(result, 2)
    except ZeroDivisionError:
        return None


def performance_assessment(average_grade: float) -> str:
    """
    - Принимает средний балл студента
    - Если средний балл 75 и выше возвращает True иначе False
    """
    if not average_grade:
        return 'Нет оценок'
    elif average_grade >= 75:
        return 'Успешен'
    return 'Не успешен'

def calculate_average_all_students(all_students_list: list[dict[str, list[int]]]) -> float:
    """
    - Получает список всех студентов
    - Возвращает средний балл всех студентов
    """
    all_students_grades = []
    for student in all_students_list:
        all_students_grades += student['grades']
    result = sum(all_students_grades) / len(all_students_grades)

    print(f'Средний балл всех студентов:\n{round(result, 2)}\n')
    return round(result, 2)

def get_student_info(student_name: str, avg_grade: float, performance: str) -> str:
    """
    Принимает данные студента, оформляет и отдает их единой строкой
    """
    return (f'Студент: {student_name}\n'
            f'Средний балл: {avg_grade}\n'
            f'Статус: {performance}\n')

def add_new_student(
        new_student: dict[str, list[int]],
        all_students_list: list[dict[str, list[int]]]
) -> str | list[dict[str, list[int]]]:
    """
    - Принимает словарь студента и список всех студентов
    - Добавляет нового студента и возвращает измененный список студентов
    """
    all_students_list.append(new_student)

    print(f'Добавлен новый студент - {new_student["name"]}')
    return all_students_list

def delete_student(
        student: dict[str, list[int]],
        all_students_list: list[dict[str, list[int]]]
) -> str | list[dict[str, list[int]]]:
    """
    - Принимает словарь студента и список всех студентов
    - Удаляет студента и возвращает измененный список студентов
    """
    all_students_list.remove(student)

    print(f'Удален студент - {student["name"]}')
    return all_students_list
