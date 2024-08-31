from app.models.student import Student

def test_student():
    student = Student(name="Mateus Braga", belt="white")
    assert student.color == "white"
