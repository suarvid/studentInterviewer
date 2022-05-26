#!/usr/bin/env python
# -*- coding: utf-8 -*-
import speech_recognition as sr
import sys

class Question:
    def __init__(self, data, correct_answer_tokens, weight=1.0):
        self.left = None
        self.right = None
        self.data = data
        self.weight = weight
        self.answer_score = 0.0
        self.correct_answer_tokens = correct_answer_tokens
        self.recognizer = sr.Recognizer()

    def add_left_child(self, leftChild):
        self.left = leftChild

    def add_right_child(self, rightChild):
        self.right = rightChild

    def evaluate(self):
        response = self.ask_question()
        score = self.evaluate_response(response.lower())
        self.answer_score += score * self.weight
        if score > 0 and self.left is not None:
            self.left.evaluate()
        if score < 0 and self.right is not None:
            self.right.evaluate()
        else:
            return  # Will move on to the next tree in the calling function

    def ask_question(self):
        with sr.Microphone() as source:
            print("QUESTION:")
            print(self.data)
            audio = self.recognizer.listen(source)
            try:
                return self.recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                return "Unknown"
            except sr.RequestError as e:
                print(f"Sphinx error: {e}")

    def evaluate_response(self, response):
        response_tokens = response.split()
        for token in response_tokens:
            if token in self.correct_answer_tokens:
                print(f"GOOD RESPONSE: {response}")
                return 1
        print(f"BAD RESPONSE: {response}")
        return -1

    def get_tree_score(self):
        score = 0.0
        if self.left is not None:
            get_tree_score(self.left)
        if self.right is not None:
            get_tree_score(self.right)
        score += self.answer_score
        return score

