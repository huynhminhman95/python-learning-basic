from quiz import Quiz
question = [
    "Cau 1. Doi bong nao ve nhi World cup 1994?\nA. Brazil \nB. Italia \nC. Duc\n",
    "Cau 2. Doi bong nao vo dich Wolrd cup 1998?\nA. Argentina \nB. Phap \nC. Brazil\n",
    "Cau 3. Nuoc nao la chu nha Wolrd cup 2002?\nA. Qatar \nB. Duc \nC. HanQuoc + Nhatban\n",
]

quizzes = [
    Quiz(question[0], "B"),
    Quiz(question[1], "B"),
    Quiz(question[2], "C"),
]

def run_quizzes(quizzes):
    score = 0
    for quiz in quizzes:
        print(quiz.question)
        user_input = input("Nhap cau tra loi cua ban: ")
        if user_input.lower() == quiz.answer.lower():
            score += 1
    print(f"\n --> Ket qua: ban da tra loi dung {score}/{len(quizzes)} cau.")

run_quizzes(quizzes)