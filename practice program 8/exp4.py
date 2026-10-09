import shlex


class Question:
    def __init__(self, question, correct_answer, student_answer, points):
        self.question = question
        self.correct_answer = correct_answer
        self.student_answer = student_answer
        self.points = points

    def grade(self):
        pass


class MCQ(Question):
    def grade(self):
        if self.student_answer == self.correct_answer:
            return self.points
        return 0


class TF(Question):
    def grade(self):
        if self.student_answer == self.correct_answer:
            return self.points
        return 0


class Essay(Question):
    def grade(self):
        keywords = self.correct_answer.split(",")
        answer = self.student_answer.lower()

        count = 0

        for keyword in keywords:
            if keyword.strip().lower() in answer:
                count += 1

        if count >= 2:
            return self.points * 0.75
        elif count == 1:
            return self.points * 0.50
        else:
            return 0


n = int(input())
total = 0

for i in range(n):
    data = shlex.split(input())

    question_type = data[0]
    question_text = data[1]
    correct_answer = data[2]
    student_answer = data[3]
    points = int(data[4])

    if question_type == "MCQ":
        question = MCQ(
            question_text,
            correct_answer,
            student_answer,
            points
        )

    elif question_type == "TF":
        question = TF(
            question_text,
            correct_answer,
            student_answer,
            points
        )

    else:
        question = Essay(
            question_text,
            correct_answer,
            student_answer,
            points
        )

    score = question.grade()
    total += score

    print(f"{question_type}: {score:.2f}")

print(f"Total Score: {total:.2f}")