#!/usr/bin/python3
"""A Quiz Game Module"""
from quiz_brain import QuizBrain
from quiz_data import question_data
from quiz_model import Question
from os import system, name


def clear():
    """A command used to clear the screen"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Create a list of Questions (from quiz_model) taken from the question_data (from quiz_data)
question_bank = [Question(q['text'], q['answer']) for q in question_data]

def quiz_game():
    """Start Quiz Game"""
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        clear()
        quiz.next_question()
        input("Press enter to continue")
    print(f" You got {quiz.score} out of {quiz.question_num}!!")
    play_again = input("Do you want to play again? Type 'y' to play again! or 'n' to exit: ").lower()
    if play_again == "y":
        quiz_game()
    else:
        print("Thanks for playing. Bye!")
        return

quiz_game()

