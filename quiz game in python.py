questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": 1
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yen", "Dollar", "Euro", "Pound"],
        "answer": 0
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"],
        "answer": 3
    },
    {
        "question": "What is the highest mountain in the world?",
        "options": ["Mount Kilimanjaro", "Mount Everest", "Mount Fuji", "Mount Blanc"],
        "answer": 1
    }
]

def play_quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(i + 1, ")", option)
        answer = int(input("Enter your answer: "))
        if answer == question["answer"] + 1:
            score += 1
            print("Correct!")
        else:
            print("Incorrect.")
    print("\nYour score is: ", score, " out of ", len(questions))

play_quiz(questions)
