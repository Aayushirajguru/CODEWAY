import random

def load_questions():

    questions = [
        {
            'question': 'What is the capital of India?',
            'choices': ['A. Mumbai', 'B. Kolkata', 'C. Delhi', 'D. Chennai'],
            'correct_answer': 'C'
        },
        {
            'question': 'Which river is considered the holiest river in Hinduism?',
            'choices': ['A. Yamuna', 'B. Ganges', 'C. Brahmaputra', 'D. Godavari'],
            'correct_answer': 'B'
        },
        {
            'question': 'Who was the first Prime Minister of India?',
            'choices': ['A. Jawaharlal Nehru', 'B. Indira Gandhi', 'C. Rajiv Gandhi', 'D. Sardar Patel'],
            'correct_answer': 'A'
        },
        {
            'question': 'Which famous Indian monument is known as the "Symbol of Love"?',
            'choices': ['A. Qutub Minar', 'B. India Gate', 'C. Taj Mahal', 'D. Charminar'],
            'correct_answer': 'C'
        },
        {
            'question': 'In which year did India gain independence?',
            'choices': ['A. 1942', 'B. 1947', 'C. 1950', 'D. 1962'],
            'correct_answer': 'B'
        },
        {
            'question': 'What is the national currency of India?',
            'choices': ['A. Rupee', 'B. Rupiah', 'C. Baht', 'D. Ringgit'],
            'correct_answer': 'A'
        },
        {
            'question': 'Which festival is known as the "Festival of Lights" in India?',
            'choices': ['A. Holi', 'B. Diwali', 'C. Eid', 'D. Navratri'],
            'correct_answer': 'B'
        },
        {
            'question': 'Who is known as the "Father of the Nation" in India?',
            'choices': ['A. Jawaharlal Nehru', 'B. Subhas Chandra Bose', 'C. Mahatma Gandhi', 'D. Bhagat Singh'],
            'correct_answer': 'C'
        },
        {
            'question': 'Which Indian state is known as the "Land of Five Rivers"?',
            'choices': ['A. Punjab', 'B. Haryana', 'C. Uttar Pradesh', 'D. Rajasthan'],
            'correct_answer': 'A'
        },
        {
            'question': 'Which Indian city is famous for its IT industry and is known as the "Silicon Valley of India"?',
            'choices': ['A. Hyderabad', 'B. Pune', 'C. Bengaluru', 'D. Ahmedabad'],
            'correct_answer': 'C'
        },
        # Add more questions as needed
    ]

    return questions

def present_question(question):
    print("\n" + question['question'])
    for choice in question['choices']:
        print(choice)

    user_answer = input("Enter the letter of your choice: ").upper()
    return user_answer

def evaluate_answer(user_answer, correct_answer):
    return user_answer == correct_answer

def display_result(score, total_questions):
    print(f"\nYour Final Score: {score}/{total_questions}")
    print("Thanks for playing!")

def quiz_game():
    print("\nWelcome to the Quiz Game!")
    print("Answer the following questions by entering the letter of your choice (A, B, C, D).")

    questions = load_questions()
    total_questions = len(questions)
    score = 0

    for question in random.sample(questions, total_questions):
        user_answer = present_question(question)
        if evaluate_answer(user_answer, question['correct_answer']):
            print("Correct! Well done.")
            score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer is: {question['correct_answer']}")

    display_result(score, total_questions)

# Main program
while True:
    quiz_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Goodbye!")
        break
