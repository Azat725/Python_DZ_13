import random


def print_grade(marks: list) -> list:
    # Вывод оценок (вывод содержимого списка)

    return marks


def retake_exam(marks: list, id_of_mark: int, new_mark: int) -> list:
    # Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку)

    marks[id_of_mark] = new_mark
    return marks


def sholarship(marks: list) -> bool:
    # Выходит ли стипендия (стипендия выходит, если средний бал не ниже 10.7)

    result = sum(marks) / float(len(marks))

    if result >= 10.7:
        student_receive_sholarship = True
    else:
        student_receive_sholarship = False

    return student_receive_sholarship


def descending_sort(marks: list) -> list:
    # Вывод отсортированного списка по убыванию

    for i in range(len(marks)):
        for j in range(i + 1, len(marks)):
            if marks[i] > marks[j]:
                marks[i], marks[j] = marks[j], marks[i]
    return marks


def ascending_sort(marks: list) -> list:
    # Вывод отсортированного списка по возрастанию

    for i in range(len(marks)):
        for j in range(0, len(marks) - 1):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
    return marks

marks = [random.randint(1, 12) for _ in range(10)]

first_print = print_grade(marks)
print(f"Оценки -> {first_print}")
print()

id_of_mark = int(input("Введите оценку которую хотите изменить -> "))
new_mark = int(input("Введите на какую оценку вы хотите изменить -> "))
second_print = retake_exam(marks, id_of_mark, new_mark)
third_print = sholarship(marks)
fourth_print = descending_sort(marks)
fifth_print = ascending_sort(marks)

print(f"Оценки -> {first_print}")
print()

print(f"Оценки после пересдачи -> {second_print}")
print()

print(f"Выходит ли стипендия -> {third_print}")
print()

print(f"Отсортированный список по убыванию -> {fourth_print}")
print()

print(f"Отсортированный список по возрастанию -> {fifth_print}")