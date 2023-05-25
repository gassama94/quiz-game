import time
print("Welcome to my Quiz Game!")

playing = input("Do you want to play? (yes/no): \n").lower()
if playing != "yes":
    quit()

print("Great! Let's play!")

questions = {
    "France": "Paris",
    "England": "London",
    "Norway": "Oslo",
    "Italy": "Rome",
    "Sweden": "Stockholm",
    "Spain": "Madrid",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Netherlands": "Amsterdam",
    "Portugal": "Lisbon"
}


total_questions = len(questions)
correct_answers = 0
total_time = 0


for country, capital in questions.items():
    start_time = time.time() 
    answer = input(f"What is the capital city of {country}? \n").lower()
    end_time = time.time() 
    question_time = end_time - start_time  # Time taken to answer the question
    if answer == capital.lower():
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect Answer!")

    print(f"Time taken: {question_time:.2f} seconds\n")
    total_time += question_time

# print(f"\nQuiz completed! You scored {score} out of {len(questions)}.")
print("\nQuiz Summary")
print("--------------")
print(f"Total Questions: {total_questions}")
print(f"Correct Answers: {correct_answers}")
print(f"Total Time: {total_time:.2f} seconds")

if correct_answers >= 6:
    print("Congratulations! You passed the game.")
else:
    print("Sorry! You failed the game.")
