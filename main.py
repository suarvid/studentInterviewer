#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Read in questions, answers and follow-up questions from file here
def generate_topics():
    pass


if __name__ == "__main__":
    topics = generate_topics()
    for topic in topics:
        topic.evaluate_topic()
