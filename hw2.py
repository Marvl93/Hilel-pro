storage: list[dict] = [
    {
        "id": 1,
        "name": "John Doe",
        "marks": [4, 12, 8, 2, 3],
        "info": "John is 20y.o. Interests: play tennis"
    },
    {
        "id": 2,
        "name": "Marry Fin",
        "marks": [11, 2, 3, 5, 8],
        "info": "John is 21y.o. Interests: dancing"
    },
    {
        "id": 3,
        "name": "Hanry Odego",
        "marks": [1, 2, 7, 9, 10],
        "info": "John is 20y.o. Interests: boxing"
    },
    {
        "id": 4,
        "name": "Terry Henry",
        "marks": [11, 12, 9, 10, 7],
        "info": "John is 20y.o. Interests: play footbal"
    },
    {
        "id": 5,
        "name": "Markus Low",
        "marks": [4, 6, 9, 10, 1],
        "info": "John is 20y.o. Interests: reading books"
    },
    {
        "id": 6,
        "name": "Any Anyston",
        "marks": [9, 5, 2, 11, 12],
        "info": "John is 20y.o. Interests: artist"
    }
]

#CRUD
def add_student (student: dict) -> dict | None:
   if len(student) != 2:
       return None

   if not student.get("name") or not student.get("marks"):
       return None
   else:
       storage.append(student)
       return student

def show_students():
    print("=========================\n")
    for index, student in storage:
            print(f"{student['id']}. Student {student['name']}\n")
    print("=========================\n")

def search_student(student_id: str) -> None:
    for student in storage:
        info = (
        "=========================\n"
        f"[{student['id']}] Student {student['name']}\n"
        f"Marks: {student['marks']}\n"
        f"Info: {student['info']}\n"
        "=========================\n"
    )
        if student['id'] == student_id:
            print(info)
            return
    print(f"Student {student_id} not found")

def ask_student_payload() -> dict:
    ask_prompt = (
        "Enter student's payload data using text template:"
        "John Doe; 1,2,3,4,5\n"
        "where 'John Doe' is a full name and [1,2,3,4,5] are marks.\n"
        "The data must be separated by ';'"
    )
    def parse(data) -> dict:
      name, raw_marks = data.split(";")
      return {
          "name": name,
          "marks": [int(item) for item in raw_marks.replace(" ", "").split(",")],
      }

    user_data: str = input(ask_prompt)
    return parse(user_data)

def student_management_command_handle(command: str):
    if command == "show":
            show_students()
    elif command == "add":
        data = ask_student_payload()
        if data:
            student: dict | None = add_student(data)
            print(f"Student: {student['name']} is added")
        else:
            print("The student's data is NOT correct. Please try again")
    elif command == "search":
        student_id: str = input("\nEnter student's ID:")
        if student_id:
            search_student(student_id=int(student_id))
        else:
            print("Student's name is required to search")

def handler_user_input():
    OPERATION_COMMANDS = ("quit", "help")
    STUDENR_MANAGEMENT_COMMANDS = ("show", "add", "search")
    AVAILABLE_COMMANDS = (*OPERATION_COMMANDS, *STUDENR_MANAGEMENT_COMMANDS)

    HELP_MESSAGE = (
        "Hello in the Journal! User the menu to interact with the application. \n"
        f"Avalible commands: {AVAILABLE_COMMANDS}"
    )

    print(HELP_MESSAGE)

    while True:
        command = input("\n Select command: ")

        if command == "quit":
            print("\n Thanks for using the Journal application")
            break
        elif command == "help":
            print(HELP_MESSAGE)
        else:
            student_management_command_handle(command)

if __name__ == "__main__":
    handler_user_input()