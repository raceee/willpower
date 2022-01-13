import matplotlib as plt
import numpy as np
import datetime


class LinkedList:
    def __init__(self) -> None:
        self.score = 0
        self

class Goal:
    def __init__(self, goal_name:str) -> None:
        self.goal_name = goal_name
        self.amnesty = self.set_amnesty()
        self.goal_chain = self.make_goal()

    def make_goal(self) -> LinkedList:
        return LinkedList()
    
    def set_amnesty(self) -> int:
        return int(input("How many days of amnesty do you want for this goal: "))

class Profile:
    def __init__(self, name:str) -> None:
        self.name = name
        self.goals = []

    def new_goal(self) -> list:
        return self.goals.append(Goal())