from app.models.student import Student

def test_student__white_belt():
    student = Student(name="Mateus Braga")

    assert student.belt == "white"
    assert student.stripes == 0
    assert student.moves == []
    
def test_student__learn_new_move():
    student = Student(name="Mateus Braga")
    student.learn_move('arm-lock')

    assert student.moves == ['arm-lock']
