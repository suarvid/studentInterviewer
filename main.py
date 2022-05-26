#!/usr/bin/env python
# -*- coding: utf-8 -*-

from question_tree import Question
from topic import Topic

# Read in questions, answers and follow-up questions from file here
def generate_topics():
    # Vad är det som behöver skapas här?
    # Några topics, t.ex börja med ett
    # Vad behöver ett topic?
    # Ett eller fler frågeträd
    # Vad behöver ett frågeträd?
    # Ett frågeträd är bara en massa Question-noder
    # Så gör bara en massa question-noder för att testa
    q1 = Question("What colour is the sky?", ["blue"])
    q2 = Question("What day is between Monday and Wednesday?", ["tuesday"]) 
    q1.add_left_child(q2)
    t = Topic([q1])
    return [t]


if __name__ == "__main__":
    topics = generate_topics()
    for topic in topics:
        topic.evaluate_topic()
