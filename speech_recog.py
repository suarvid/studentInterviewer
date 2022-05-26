#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
import sys

class SpeechRecognizer():
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def get_audio_response():
        with sr.Microphone() as source:
            print("Say something!")
            audio = self.recognizer.listen(source)
            try:
                return self.recognizer.recognize_sphinx(audio)
            except sr.UnknownValueError:
                return "Unknown"
            except sr.RequestError as e:
                print(f"Sphinx error: {e}")
