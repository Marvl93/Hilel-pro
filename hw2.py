students: list[dict] = []

def show_students():
    """Виводить інформацію про всіх студентів."""
    if not students:
        print("Список студентів порожній.")
        return
    print("\nСписок студентів:")
    for student in students:
        print(f"======================="
              f"\nID: {student['id']}, Ім'я: {student['name']}")

def show_student(student_id: int = None, student_name: str = None):
    """Виводить інформацію про студента за його ID або іменем."""
    found = False
    if student_id is not None:
        for student in students:
            if student['id'] == student_id:
                print("==============================")
                print(f"Інформація про студента (ID {student_id}):")
                print(f"ID: {student['id']}")
                print(f"Ім'я: {student['name']}")
                print(f"Оцінки: {student['marks']}")
                print(f"Додаткова інформація: {student['info']}")
                print("==============================")
                return
    if student_name is not None:
        found_by_name = False
        for student in students:
            if student['name'] == student_name:
                print("==============================")
                print(f"Інформація про студента (ім'я '{student_name}'):")
                print(f"ID: {student['id']}")
                print(f"Ім'я: {student['name']}")
                print(f"Оцінки: {student['marks']}")
                print(f"Додаткова інформація: {student['info']}")
                print("==============================")
                found = True
                found_by_name = True
        if found_by_name:
            return

    if not found:
        print("Студента не знайдено")


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

def menu():
    while True:
        print("\nПривіт, в нашому журналі! Оберіть дію:")
        print("1. Показати всіх студентів")
        print("2. Показати детальну інформацію про студента")
        print("3. Додати нового студента")
        print("4. Вийти")

        choice = input("> ")

        if choice == '1':
            show_students()
        elif choice == '2':
            search_term = input("Введіть ID або ім'я студента: ")
            try:
                student_id = int(search_term)
                show_student(student_id=student_id)
            except ValueError:
                show_student(student_name=search_term)
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

if __name__ == "__main__":
    menu()