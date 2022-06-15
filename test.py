from calendar import c
from main import Question, Student

question_prompts = [
    "What is the color of the sky? \n(a) blue \n(b) green \n(c) red \n> ",
    "\n\n What is the color of the grass? \n(a) blue \n(b) green \n(c) red \n> ",
    "\n\n What is the color of the sun? \n(a) blue \n(b) green \n(c) red \n> ",
    "\n\n What is the color of the moon? \n(a) blue \n(b) green \n(c) red \n> ",
    "\n\n What is the color of the earth? \n(a) blue \n(b) green \n(c) red \n> \n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b"),
]
def get_name():
    name = input("What is your name? \n> \n\n")

    return name

name = Student(get_name(), "Math")


def run_test(questions):
    print(f"Hi {name.name}, let's test your knowledge on math! \n Input only the correct letters")
    score = 0
    
    for question in questions:
        answer = input(question.prompt).lower()
        if answer == question.answer:
            score += 1
    name.score = score
    return (f"You got {score} out of {len(questions)} correct.")


print(run_test(questions))
print()
print(name)
