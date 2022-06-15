class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Student:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.score = 0

    def __str__(self):
        return f"{self.name} got {self.score} on {self.subject}"

