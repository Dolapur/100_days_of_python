#!/usr/bin/python3
"""Quiz brain module"""
from quiz_model import Question


class QuizBrain:
    def __init__(self, question_list):
        """Intialize the starting values"""
        self.question_num = 0
        self.question_list = question_list
        self.score = 0
    
    def check_answer(self, player_answer, current_question):
        """check if the answer is correct"""
        if current_question.answer == player_answer:
            return True
        return False

    def next_question(self):
        """"Prompt player to answer the question"""
        current_question = self.question_list[self.question_num]
        player_answer = input(f"Q.{self.question_num + 1}: {current_question.text}. (True/False)?: ")
        self.question_num += 1
        
        if self.check_answer(player_answer, current_question):
            self.score += 1
            print("You're Correct")
        else:
            print("You're Wrong")
        print(f" Current Score: {self.score}/{self.question_num}.\n")

    def still_has_questions(self):
        '''Check if there are more questions'''
        if self.question_num < len(self.question_list):
            return True
        return False
