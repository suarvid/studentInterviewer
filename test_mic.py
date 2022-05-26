#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
import sys

if __name__ == "__main__":
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        print("Say something!")
        audio = recognizer.listen(source)
        try:
            response = recognizer.recognize_google(audio)
            print(response)
        except sr.UnknownValueError:
            print("Unknown")
        except sr.RequestError as e:
            print(f"Sphinx error: {e}")
