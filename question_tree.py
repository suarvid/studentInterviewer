#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time


class Question:
    def __init__(self,
                 data,
                 correct_answer_tokens,
                 related_questions=[],
                 weight=1.0):
        self.left = None
        self.right = None
        self.data = data
        self.weight = weight
        self.answer_score = 0.0
        self.correct_answer_tokens = correct_answer_tokens
        self.related_questions = related_questions
        self.answered_correctly = False

    def add_left_child(self, leftChild):
        self.left = leftChild

    def add_right_child(self, rightChild):
        self.right = rightChild

    def evaluate(self, furhat):
        response = self.ask_question(furhat)
        score = self.evaluate_response(response, furhat)
        self.answer_score += score * self.weight
        if score > 0 and self.left is not None:
            self.left.evaluate(furhat)
        if score < 0 and self.right is not None:
            self.right.evaluate(furhat)
        else:
            return  # Will move on to the next tree in the calling function

    def ask_question(self, furhat):
        furhat.say(text=self.data)
        time.sleep(2.4)
        result = furhat.listen()
        print(result, file=sys.stderr)
        return result.message.lower()

    def evaluate_response(self, response, furhat):
        response_tokens = response.split()
        for token in response_tokens:
            if token in self.correct_answer_tokens:
                furhat.say(text="Yes, that's correct!")
                furhat.gesture(name="Smile")
                time.sleep(2.0)
                self.answered_correctly = True
                return 1
        print(f"BAD RESPONSE: {response}")
        print("I'm sorry, that's not quite correct.")
        furhat.say(text="I'm sorry, that is not quite correct.")
        furhat.gesture(name="ExpressSad")
        time.sleep(2.0)
        return -1

    def get_tree_score(self):
        score = 0.0
        if self.left is not None:
            score += self.left.get_tree_score()
        if self.right is not None:
            score += self.right.get_tree_score()
        score += self.answer_score
        score += self.calculate_inconsistency_penalties()
        return score

    def calculate_inconsistency_penalties(self):
        total_penalty = 0.0
        if not self.answered_correctly:
            for (question, penalty) in self.related_questions:
                if not question.answered_correctly:
                    return 0.0
                total_penalty += penalty

        return total_penalty
