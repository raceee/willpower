import matplotlib as plt
import numpy as np
import datetime


class Goal:
    def __init__(self, goal_name:str) -> None:
        self.goal_name = goal_name
        self.goal_score = 0
        self.amnesty = self.set_amnesty()
        self.goal_chain = []
        self.used_amnesty = 0
    
    def set_amnesty(self) -> int:
        return int(input("How many days of amnesty do you want for this goal: "))
    
    def get_score(self) -> int:
        return self.goal_score
    
    def get_amnesty(self) -> int:
        return self.amnesty
    
    def get_used_amnesty(self) -> int:
        return self.used_amnesty
    
    def get_successes(self) -> int:
        return
    
    def get_misses(self) -> int:
        return
    
    def get_streak(self) -> int:
        return
    
    def get_days_on_goal(self) -> int:
        return

    def summary(self) -> None:
        print("Goal Name: {}\n Current Goal Score: {}\n Amnesty Allowance: {}\n Amnesty Used: {}\n Total Success: {}\n Total Missed: {}\n Current Streak: {}\n Days on Goal: {}".format(self.goal_name, self.get_score(), self.get_amnesty(), self.get_used_amnesty(), ))
    
    def vis_goal(self) -> None:
        pass


class Profile:
    def __init__(self, name:str) -> None:
        self.name = name
        self.goals = []

    def new_goal(self) -> list:
        return self.goals.append(Goal())

if __name__ == "__main__":
    print("hi")