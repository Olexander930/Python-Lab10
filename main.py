# Функція для відкриття файлу
def open_file(filename):
    try:
        file = open(filename, "w")
        print("Файл успішно відкрито!")
        return file
    except Exception as e:
        print(f"Не вдалося відкрити файл! Помилка: {e}")
        return None

# Функція для запису рядків у файл
def write_to_file(file):
    file = open_file(filename)
    if file is not None:
        try:

            # (Стешенко Станіслав КН-31.1)
            file.write("Стешенко Станіслав КН-31.1\n")
            file.write("Питання 1: Як вивести текст на екран у Python?\n")

            # Закриття файлу після запису
            file.close()
            print("Дані успішно записані у файл.")
            print("Файл успішно закрито!")
        except Exception as e:
            print(f"Виникла помилка під час запису у файл: {e}")
    else:
        print("Файл не було відкрито, запис неможливий.")

# (Стешенко Станіслав КН-31.1)
# Виклик функцій
filename = "Lab-10.txt"
write_to_file(filename)

# Іванченко Олексадр КН-33-2
# Відкриваємо файл у режимі дозапису і додаємо відповідь нга питання, і записую своє
def append_answer_and_question(filename, student_name, answer, question_for_next):
    try:
        with open(filename, "a") as file:  # Використовую режим "a", він  дозволяє дозаписувати, не перезаписуючи файл
            file.write(f"{student_name}\n")
            file.write(f"Відповідь: {answer}\n")
            file.write(f"Питання для наступного студента: {question_for_next}\n\n")
        print("Відповідь та нове питання успішно додані до файлу.")
    except Exception as e:
        print(f"Не вдалося додати дані до файлу! Помилка: {e}")

student_name = "Іванченко Олександр КН-33.2"
answer = "Щоб вивести текст на екран у Python, використовуйте функцію print(), ця функція приймає текст або інші дані в якості аргументів')."
question_for_next = "Які основні типи даних використовуються у Python?"

# Виклик функції для дозапису у файл
append_answer_and_question(filename, student_name, answer, question_for_next)