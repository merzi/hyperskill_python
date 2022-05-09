class Student:
    name: str
    last_name: str
    birth_year: int
    student_id: str

    def __init__(self, name: str, last_name: str, birth_year: int):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = self.calculate_student_id()

    def calculate_student_id(self) -> str:
        return self.name[0] + self.last_name + str(self.birth_year)


given_name: str = input()
given_last_name: str = input()
given_birth_year: int = int(input())
student = Student(given_name, given_last_name, given_birth_year)
print(student.student_id)
