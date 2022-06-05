#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Topic:
    def __init__(self, name, threshold, question_trees):
        self.name = name
        self.threshold = threshold
        self.score = 0
        self.q_trees = question_trees
        self.current_q_tree_index = 0

    # Oklart om detta behövs tbh
    def next_question_tree(self):
        self.current_q_tree_index += 1
        if self.q_trees[self.current_q_tree_index] is not None:
            return (True, self.q_trees[self.current_q_tree_index])
        return (False, None)

    def evaluate_topic(self, furhat):
        furhat.say(text=f"Okay, let's discuss {self.name}")
        for q_tree in self.q_trees:
            q_tree.evaluate(furhat)
        self.score = self.get_topic_score()

    def get_topic_score(self):
        score = 0.0
        for q_tree in self.q_trees:
            score += q_tree.get_tree_score()
        return score
