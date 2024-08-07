def ask_question(question, options, correct_answer):            #function to ask questions to the user
    print(question)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    while True:
        try:
            answer = int(input("Enter the number of your answer: "))
            if answer < 1 or answer > len(options):
                raise ValueError                                   #error raised in case user enters an invalid option
            break
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the options.")
    return answer == correct_answer

def run_quiz(quiz):                             #function to have a track of score and display the score at the end of the quiz
    score = 0
    for question, options, correct_answer in quiz:
        if ask_question(question, options, correct_answer):
            print("Correct!\n")
            score += 4
        else:
            print(f"Incorrect! The correct answer was {correct_answer}. {options[correct_answer-1]}\n")
    print(f"Your final score is {score} out of {4*len(quiz)}.")

def main():                                     #main function which contains the questions
    quiz = [
        ("Q1.What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3),
        ("Q2.Which planet is also known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], 2),
        ("Q3.Which among the following is the largest ocean on Earth?", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], 4),
        ("Q4.Who is the current Prime Minister of India?", ["Rahul Gandhi", "Narendra Modi", "Amit Shah", "Jawaharlal Nehru"],2),
        ("Q5.Which Indian Captain has won all the ICC trophies??", ["M S Dhoni", "Virat Kohli", "Rohit Sharma", "Sachin Tendulkar"],1),
        ("Q6.According to World Happiness Index 2024, which is the most happiest country?", ["India", "Finland", "Pakistan", "Netherlands"],2),
        ("Q7.Which among the following is the most literate state in India", ["Bengaluru", "Uttar Pradesh","Kerala","Bihar"],3),
        ("Q8.What is the Earth's innermost layer called as?", ["Core", "Crust", "Mantle","Sub Soil"],1),
        ("Q9.The Upper House of Indian Parliament is known as –", ["The Rajya Sabha", "The Lok Sabha", "The Vidhan Sabha", "The Vidhan Parishad"],1),
        ("Q10.The first British Viceroy of India", ["Lord Kargen", "Lord Irvin", "Lord Cannon", "Lord Tom"], 3)
    ]
    run_quiz(quiz)

if __name__ == "__main__":
    main()
