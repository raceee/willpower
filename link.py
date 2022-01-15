import matplotlib as plt
import numpy as np
import datetime

class Day:
    def __init__(self) -> None:
        self.score = 0

class Goal:
    def __init__(self, goal_name:str) -> None:
        self.goal_name = goal_name
        self.amnesty = self.set_amnesty()
        self.goal_chain = [Day()]
        self.used_amnesty = 0
        self.goal_score = 0
    
    def set_amnesty(self) -> int:
        return int(input("How many days of amnesty do you want for this goal: "))
    
    def get_score(self) -> int:
        # checks the last block in chain
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
        print("Goal Name: {}\n Current Goal Score: {}\n Amnesty Allowance: {}\n Amnesty Used: {}\n Total Success: {}\n Total Missed: {}\n Current Streak: {}\n Days on Goal: {}" \
        .format(self.goal_name, self.get_score(), self.get_amnesty(), self.get_used_amnesty(), self.get_successes(), self.get_misses(), self.get_streak(), self.get_days_on_goal()))
    
    def vis_goal(self) -> None:
        pass


class Profile:
    def __init__(self, name:str) -> None:
        self.name = name
        self.goals = []

    def new_goal(self, goal_name:str) -> list:
        return self.goals.append(Goal(goal_name))

if __name__ == "__main__":
    print("hi")
    race_peterson = Profile("Race Peterson")
    race_peterson.new_goal("Sleep")
    race_peterson.goals[0].summary()