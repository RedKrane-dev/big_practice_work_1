# 2
def calculate_average(grades: list[int]) -> float:
    """
    Принимает список оценок студента и возвращает среднее значение
    """
    result = sum(grades) / len(grades)
    return round(result, 2)

# 3
def performance_assessment(average_grade: float) -> str:
    """
    - Принимает средний балл студента
    - Если средний балл 75 и выше возвращает True иначе False
    """
    if average_grade >= 75:
        return 'Успешен'
    return 'Не успешен'

# 2
def calculate_average_all_students(all_students_list: list[dict[str: str, str: list[int]]]) -> float:
    """
    - Получает список всех студентов
    - Возвращает средний балл всех студентов
    """
    all_students_grades = []
    for student in all_students_list:
        all_students_grades += student['grades']
    result = sum(all_students_grades) / len(all_students_grades)
    return round(result, 2)
