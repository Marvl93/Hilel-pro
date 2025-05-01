students: list[dict] = []

def menu():
    while True:
        print("\nПривіт, в нашому журналі! Оберіть дію:")
        print("1. Показати всіх студентів")
        print("2. Показати студента за ID")
        print("3. Додати нового студента")
        print("4. Вийти")

        choice = input("> ")

        if choice == '1':
            show_students()
        elif choice == '2':
            student_id_str = input("Введіть ID студента: ")
            try:
                student_id = int(student_id_str)
                show_student(student_id)
            except ValueError:
                print("Будь ласка, введіть ціле число для ID.")
        elif choice == '3':
            name = input("Введіть ім'я студента: ")
            marks_str: str = input ("Введіть оцінки студента через кому: ")
            details = input("Введіть додаткову інформацію про хобі, інтереси тощо (необов'язково): ")
            add_student(name, marks_str, details)
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Будь ласка, спробуйте ще раз.")

def show_students():
    """Виводить інформацію про всіх студентів."""
    if not students:
        print("Список студентів порожній.")
        return
    print("\nСписок студентів:")
    for student in students:
        print(f"======================="
              f"\nID: {student['id']}, Ім'я: {student['name']}, \nОцінки: {student['marks']}, "
              f"Додаткова інформація: {student['info']}")

def show_student(student_id: int):
    """Виводить інформацію про студента за його ID."""
    for student in students:
        if student['id'] == student_id:
            print(f"\nІнформація про студента з ID {student_id}:")
            print(f"ID: {student['id']}")
            print(f"Ім'я: {student['name']}")
            print(f"Оцінки: {student['marks']}")
            print(f"Додаткова інформація: {student['info']}")
            return
    print(f"Студента з ID {student_id} не знайдено.")

def add_student(name: str, marks_str: str, details: str | None):
    """Додає нового студента до списку."""
    global students
    new_id = 1
    if students:
        new_id = students[-1]['id'] + 1
    try:
        marks_list = [int(mark.strip()) for mark in marks_str.split(',')]
    except ValueError:
        print("Будь ласка, введіть оцінки через кому, використовуючи цілі числа.")
        return
    new_student = {
        'id': new_id,
        'name': name,
        'marks': marks_list,
        'info': details if details is not None else ""
    }
    students.append(new_student)
    print(f"Додано Студента: -- \nID {new_id} Імʼя: {name} \nОцінки: {marks_list} "
          f"\nДодаткова інформація про студента: {details}.")

if __name__ == "__main__":
    menu()