from tts_module import read_question
from stt_module import get_answer, get_command

questions = ["What is AI?","Define ML","What are the applications of AI?"]
answers = {}
current_question = 0
total_questions = len(questions)

while current_question < total_questions:
    question = questions[current_question]
    read_question(f"Question {current_question+1}:{question}")
    command = get_command().lower()

    if "repeat" in command:
        continue
    elif "next" in command or "answer" in command:
        read_question("Please say your answer after a beep.")
        answer = get_answer()
        answers[f"Question {current_question+1}"] = answer
        current_question += 1

    elif "submit" in command:
        break
    else:
        read_question("Sorry I didn't understand. Say 'next','repeat' or 'submit'.")

with open("exam_answers.txt","w") as f:
    for q,a in answers.items():
        f.write(f"{q}\nanswer:{a}\n\n")
    read_question("Your answers have been saved. Thank you!")
