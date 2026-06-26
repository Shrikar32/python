#quiz game
questions = (
    "What is the captial of India? ",
    "What is the captial of USA? ",
    "What is the captial of UK? ",
    "What is the captial of France? ",
    "What is the captial of Germany? ",
    "What is the captial of Japan? "
)
options = (
    ("A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"),
    ("A. New York", "B. Washington D.C.", "C. Los Angeles", "D. Chicago"),
    ("A. London", "B. Manchester", "C. Birmingham", "D. Liverpool"),
    ("A. Paris", "B. Lyon", "C. Marseille", "D. Toulouse"),
    ("A. Berlin", "B. Hamburg", "C. Munich", "D. Cologne"),
    ("A. Tokyo", "B. Osaka", "C. Kyoto", "D. Nagoya")
)
answers = ("A", "B", "A", "A", "A", "A")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("------------------------------")
    print(question)

    for option in options[questions_num]:
        print(option)

    guess = input("Enter your guess for the answer: ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        score = score + 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"The answer you entered is incorrect, The correct answer is {answers[questions_num]}")

    questions_num += 1

print("----------------------------")
print("Results")
print("---------------------------")
print("Answers : ",end=" ")
for answer in answers:
    print(answer, end=" ")
print()    
print("Guesses : ",end=" ")
for guess in guesses:
    print(guess, end=" ")
print() 
print(f"Your score is  : {score} out of {len(questions)}")       
# ---------------------- HOW THIS LOOP WORKS ----------------------
#
# questions_num starts at 0, which corresponds to the first question.
#
# The outer loop:
#
#     for question in questions:
#
# automatically goes through each question in the 'questions' tuple one
# at a time. On each iteration, the variable 'question' stores the current
# question.
#
# First iteration:
#     question = questions[0]  -> "What is the capital of India?"
#
# Second iteration:
#     question = questions[1]  -> "What is the capital of USA?"
#
# Third iteration:
#     question = questions[2]  -> "What is the capital of UK?"
#
# and so on...
#
# The inner loop:
#
#     for option in options[questions_num]:
#
# prints all the options for the current question.
#
# Example:
# questions_num = 0
# options[0] = ("A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai")
#
# The inner loop prints each option one by one.
#
# After displaying the options, the user enters a guess.
#
# The guess is compared with:
#
#     answers[questions_num]
#
# Since questions_num matches the current question, the correct answer is
# checked.
#
# Example:
# questions_num = 0
# answers[0] = "A"
#
# If the guess is correct:
#
#     score += 1
#
# Otherwise, the correct answer is displayed.
#
# Finally:
#
#     questions_num += 1
#
# moves to the next index.
#
# So after Question 1:
# questions_num = 1
#
# After Question 2:
# questions_num = 2
#
# After Question 3:
# questions_num = 3
#
# This keeps all three tuples synchronized:
#
# questions[0] -> options[0] -> answers[0]
# questions[1] -> options[1] -> answers[1]
# questions[2] -> options[2] -> answers[2]
# ...
#
# In short:
# - The outer loop automatically moves through each question.
# - questions_num keeps track of which question we're on.
# - That index is used to access the matching options and correct answer.
# - questions_num is incremented at the end so the next iteration uses the
#   next question, its options, and its answer.
# ---------------------------------------------------------------