import shlex


class Question:
    def __init__(self, question_text, correct_answer, points):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.points = points

    def grade(self, student_answer):
        return 0.0


class MCQQuestion(Question):
    def grade(self, student_answer):
        if student_answer == self.correct_answer:
            return self.points
        return 0.0


class TrueFalseQuestion(Question):
    def grade(self, student_answer):
        if student_answer == self.correct_answer:
            return self.points
        return 0.0


class EssayQuestion(Question):
    def grade(self, student_answer):
        keywords = [
            word.strip().lower()
            for word in self.correct_answer.split(",")
            if word.strip()
        ]

        answer = student_answer.lower()
        matches = sum(1 for word in keywords if word in answer)

        if matches >= 2:
            return self.points * 0.75
        elif matches == 1:
            return self.points * 0.50
        return 0.0


QUESTION_TYPES = {
    "MCQ": MCQQuestion,
    "TF": TrueFalseQuestion,
    "ESSAY": EssayQuestion
}

n = int(input())
total_score = 0.0

for _ in range(n):
    parts = shlex.split(input())

    question_type = parts[0]
    question_text = parts[1]
    correct_answer = parts[2]
    student_answer = parts[3]
    points = float(parts[4])

    question = QUESTION_TYPES[question_type](
        question_text, correct_answer, points
    )

    score = question.grade(student_answer)
    print(f"{question_type}: {score:.2f}")
    total_score += score

print(f"Total Score: {total_score:.2f}")