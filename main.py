#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stderr
import time
from question_tree import Question
from topic import Topic
from furhat_remote_api import FurhatRemoteAPI

def generate_weekday_topic():
    q1 = Question("Which is the second day of the week?", ["Tuesday", "tuesday"])
    q2 = Question("Which is the last day of the week?", ["Sunday", "sunday", "some day", "some", "day", "someday"])
    q3 = Question("Which day is between Sunday and Tuesday?", ["Monday", "monday"])
    q4 = Question("Which is the first day of the week?", ["Monday", "monday"], [(q1, -2.0), (q2, -2.0), (q3, -2.0)])
    q1.add_left_child(q2)
    q1.add_right_child(q2)
    q2.add_left_child(q3)
    q2.add_right_child(q3)
    q3.add_left_child(q4)
    return Topic("The Weekdays", 6.0, [q1])

def generate_alphabet_topic():
    q1 = Question("How many letters does the english alphabet have?", ["26" ,"twenty six", "twenty", "six"])
    q2 = Question("Which is the last letter of the english alphabet?", ["zet","Zedd", "Zed", "zed", "zedd", "z", "zee", "sea", "c", "see", "sed", "set", "said", "sent"])
    q3 = Question("Which is the 26th letter of the english alphabet?", ["zet", "Zedd", "Zed", "zed", "zedd", "z", "zee", "sea", "c", "see", "sed", "set", "said", "sent"], [(q1, -3.0), (q2, -3.0)])
    q1.add_left_child(q2)
    q1.add_right_child(q2)
    q2.add_left_child(q3)
    q2.add_right_child(q3)
    return Topic("The Alphabet", 6.0, [q1])

def generate_quantum_mechanics_topic():
    q1 = Question("What is a Bloch wave?", ["bloch", "function", "bloch function", "satisfying bloch function", "block function", "satisfying block function", "schroedinger equation", "satsfying schoredinger equation"])
    q2 = Question("What is a Boson?", ["fundamental particles", "photons", "gluons", "weak interaction particles", "weak interaction", "particles", "futons", "futon"])
    q3 = Question("Could you give me some examples of fermions?", ["electrons", "quarks", "protons", "neutrons", "neutrinos"])
    q1.add_left_child(q2)
    q1.add_right_child(q2)
    q2.add_left_child(q3)
    q2.add_right_child(q3)
    return Topic("Quantum Mechanics", 6.0, [q1])


# Read in questions, answers and follow-up questions from file here
def generate_topics():
    weekday = generate_weekday_topic()
    alphabet = generate_alphabet_topic()
    quant_mechanics = generate_quantum_mechanics_topic()
    return [alphabet, weekday, quant_mechanics]


if __name__ == "__main__":
    topics = generate_topics()
    furhat = FurhatRemoteAPI("localhost")
    furhat.set_voice(name="Matthew")
    furhat.attend(user="CLOSEST")
    furhat.say(text="Hi there!")
    furhat.say(text="In this interview, we will be evaluating your knowledge in a few set topics.")
    furhat.say(text="The topics we will be discussing today are")
    for topic in topics:
        furhat.say(text=f"{topic.name}")
        time.sleep(0.5)
    furhat.say(text="Are you ready to start?")
    time.sleep(7.0)
    response = furhat.listen()
    print(response, file=stderr)
    affermative_responses = ["yes", "why not", "sure", "yeah", "yep", "yes please", "please"]
    if response.message not in affermative_responses:
        furhat.say(text="I'm sorry to hear that, please come back when you are ready.")
        exit()
    furhat.say(text="Great, let's get started!")
    time.sleep(0.5)
    for topic in topics:
        topic.evaluate_topic(furhat)
    total_score = 0.0
    threshold = 5.0
    for topic in topics:
        print(f"SCORE FOR TOPIC {topic.name}:")
        topic_score = topic.get_topic_score()
        print(topic_score)
        total_score += topic_score
    print(f"TOTAL SCORE: {total_score}")
    print(f"THRESHOLD NEEDED TO PASS: {threshold}")
    furhat.say(text="Okay, I think that's all I need.")
    furhat.say(text="Would you like to know how you did?")
    time.sleep(1.5)
    response = furhat.listen()
    if response.message in affermative_responses:
        furhat.say(text="Great! Here's your results.")
        for topic in topics:
            furhat.say(text=f"When discussing {topic.name}, you got {str(topic.score)} points, where {str(topic.threshold)} was needed to pass.")
            time.sleep(1.0)
        furhat.say(text=f"Overall, you got {str(total_score)} points, where {threshold} were needed to pass.")
    else:
        furhat.say(text="Okay then, a teaching assistant or professor will let you know how it went in the coming days.")
    furhat.say(text="Thank you for answering my questions. Have a nice day.")
