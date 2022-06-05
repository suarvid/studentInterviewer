#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Make this singleton pattern, maybe

class QuestionAsker:
    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

#    def __init__(self, topics, pass_score_threshold=0.0):
#        self.topics = topics
#        self.speech_recognizer = SpeechRecognizer()
#        self.pass_score_threshold = pass_score_threshold
#        self.user_score = 0.0

    def ask_question(self, question_data):
        print("QUESTION:")
        print(question_data)
        response = self.speech_recognizer.get_audio_response()
        return response
