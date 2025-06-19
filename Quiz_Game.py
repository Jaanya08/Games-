def welcome():
    print("🧠 Welcome to the Python Quiz Game!")
    print("You will be asked 5 questions.")
    print("Type the letter (a/b/c/d) to answer.\n")

def get_questions():
    return {
        "What is the output of 3 * 1 ** 3?": {
            "options": {"a": "3", "b": "1", "c": "9", "d": "27"},
            "answer": "a"
        },
        "Which keyword is used for function in Python?": {
            "options": {"a": "func", "b": "define", "c": "def", "d": "function"},
            "answer": "c"
        },
        "What is the correct file extension for Python files?": {
            "options": {"a": ".pt", "b": ".py", "c": ".pyt", "d": ".p"},
            "answer": "b"
        },
        "Which data type is immutable in Python?": {
            "options": {"a": "List", "b": "Set", "c": "Tuple", "d": "Dictionary"},
            "answer": "c"
        },
        "What is the output of: print(type('Hello'))?": {
            "options": {"a": "<class 'string'>", "b": "<class 'int'>", "c": "<class 'str'>", "d": "<class 'char'>"},
            "answer": "c"
        }
    }

def ask_question(question, options, correct):
    print(f"\n❓ {question}")
    for key in sorted(options):
        print(f"  {key}) {options[key]}")
    
    while True:
        answer = input("Your answer (a/b/c/d): ").lower()
        if answer in options:
            return answer == correct
        else:
            print("Invalid input. Please enter a, b, c, or d.")

def quiz():
    welcome()
    questions = get_questions()
    score = 0

    for question, qdata in questions.items():
        if ask_question(question, qdata["options"], qdata["answer"]):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer was: {qdata['answer']}) {qdata['options'][qdata['answer']]}")

    print(f"\n🎯 Your final score is: {score}/{len(questions)}")
    if score == len(questions):
        print("🏆 Perfect! You're a Python pro!")
    elif score >= 3:
        print("👍 Good job! Keep learning.")
    else:
        print("📚 Keep practicing and try again!")

if __name__ == "__main__":
    quiz()
