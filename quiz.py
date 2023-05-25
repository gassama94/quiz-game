print("Welcome to my Quiz Game!")

playing = input("Do you want to play? (yes/no): ").lower()
if playing != "yes":
    quit()

print("Great! Let's play!")

questions = {
    "France": "Paris",
    "England": "London",
    "Norway": "Oslo",
    "Italy": "Rome",
    "Sweden": "Stockholm"
}

score = 0

for country, capital in questions.items():
    answer = input(f"What is the capital city of {country}? ").lower()
    
    if answer == capital.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect Answer!")

print(f"\nQuiz completed! You scored {score} out of {len(questions)}.")
