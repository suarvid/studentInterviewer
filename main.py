#!/usr/bin/env python
# -*- coding: utf-8 -*-

from question_tree import Question
from topic import Topic

def generate_weekday_topic():
    q1 = Question("Which is the second day of the week?", ["tuesday"])
    q2 = Question("Which is the last day of the week?", ["sunday", "some day", "some", "day", "someday"])
    q3 = Question("Which day is between Sunday and Tuesday?", ["monday"])
    q4 = Question("Which is the first day of the week?", ["monday"], [(q1, -2.0), (q2, -2.0), (q3, -2.0)])
    q1.add_left_child(q2)
    q1.add_right_child(q2)
    q2.add_left_child(q3)
    q2.add_right_child(q3)
    q3.add_left_child(q4)
    return Topic("Weekdays", [q1])

def generate_alphabet_topic():
    q1 = Question("How many letters does the english alphabet have?", ["26" ,"twenty six", "twenty", "six"])
    q2 = Question("Which is the last letter of the english alphabet?", ["zed", "z", "zee", "sea", "c", "see", "sed", "set", "said", "sent"])
    q3 = Question("Which is the 26th letter of the english alphabet?", ["zed", "z", "zee", "sea", "c", "see", "sed", "set", "said", "sent"], [(q1, -3.0), (q2, -3.0)])
    q1.add_left_child(q2)
    q1.add_right_child(q2)
    q2.add_left_child(q3)
    q2.add_right_child(q3)
    return Topic("Alphabet", [q1])


# Read in questions, answers and follow-up questions from file here
def generate_topics():
    weekday = generate_weekday_topic()
    alphabet = generate_alphabet_topic()
    return [alphabet]


if __name__ == "__main__":
    topics = generate_topics()
    for topic in topics:
        topic.evaluate_topic()
    total_score = 0.0
    threshold = 12.0
    for topic in topics:
        print(f"SCORE FOR TOPIC {topic.name}:")
        topic_score = topic.get_topic_score()
        print(topic_score)
        total_score += topic_score
    print(f"TOTAL SCORE: {total_score}")
    print(f"THRESHOLD NEEDED TO PASS: {threshold}")

