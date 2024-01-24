import random

class QuizMaker:
    def __init__(self, questions_file, key_file):
        self.questions = self.load_questions(questions_file)
        self.answer_key = self.load_answer_key(key_file)

    def load_questions(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            questions = [line.strip() for line in lines if line.strip()]
        return questions

    def load_answer_key(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            answer_key = {line.split(':')[0].strip(): line.split(':')[1].strip() for line in lines if line.strip()}
        return answer_key

    def generate_quiz(self, num_questions):
        selected_questions = random.sample(self.questions, num_questions)
        return selected_questions

    def administer_quiz(self, quiz):
        student_answers = {}
        for question in quiz:
            print(question)
            answer = input("Your answer: ").strip()
            student_answers[question] = answer
        return student_answers

    def grade_quiz(self, student_answers):
        score = 0
        for question, student_answer in student_answers.items():
            correct_answer = self.answer_key.get(question, '').strip()
            if student_answer.lower() == correct_answer.lower():
                score += 1
        return score

if __name__ == "__main__":
    questions_file = "questions.txt"  # Replace with the path to your questions file
    key_file = "answer_key.txt"  # Replace with the path to your answer key file

    quiz_maker = QuizMaker(questions_file, key_file)

    num_questions_per_quiz = 3
    quiz = quiz_maker.generate_quiz(num_questions_per_quiz)

    print("\nQuiz:")
    for idx, question in enumerate(quiz, start=1):
        print(f"{idx}. {question}")

    student_answers = quiz_maker.administer_quiz(quiz)
    score = quiz_maker.grade_quiz(student_answers)

    print(f"\nScore: {score}/{num_questions_per_quiz}")
