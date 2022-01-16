import matplotlib as plt
import numpy as np
from datetime import date
class Day:
    def __init__(self, score=0, success=True) -> None:
        self.score = 0
        self.date = date.today()
        self.success = success

class Goal:
    def __init__(self, goal_name:str) -> None:
        self.goal_name = goal_name
        self.amnesty = self.set_amnesty()
        self.amnesty_score = self.amnesty
        self.goal_chain = [Day(success=None)]
        self.goal_score = 0
    
    def make_day(self):
        input_ = str(input("Did you complete today's goal? (y/n) "))
        if input_ == "y":
            self.goal_chain.append(Day(score=self.goal_chain[len(self.goal_chain) - 1].score + 1))
            print("score inserted as ", self.goal_chain[len(self.goal_chain) - 1].score)
            self.reset_amnesty()
        elif input_ == "n":
            if self.amnesty_score != 0:
                self.amnesty_score = self.amnesty_score - 1
                self.goal_chain.append(Day(score=self.goal_chain[len(self.goal_chain) - 1].score, success=False))
                print("score inserted as ", self.goal_chain[len(self.goal_chain) - 1].score)
                print("amnesty score ", self.amnesty_score)
            else:
                si = self.goal_chain[len(self.goal_chain) - 1].score - 1
                print("si ", si)
                self.goal_chain.append(Day(score=si, success=False))
                print("score inserted as ", self.goal_chain[len(self.goal_chain) - 1].score)
                print("amnesty score ", self.amnesty_score)

    def reset_amnesty(self):
        self.amnesty_score = self.amnesty
        print("amnesty score reset")

    def set_amnesty(self) -> int:
        return int(input("How many days of amnesty do you want for this goal: "))
    
    def get_score(self) -> int:
        # checks the last block in chain
        return self.goal_chain[len(self.goal_chain) - 1].score
    
    def get_amnesty(self) -> int:
        return self.amnesty
    
    def get_used_amnesty(self) -> int:
        return self.amnesty_score
    
    def get_successes(self) -> int:
        return sum([1 for day in self.goal_chain if day.success])
    
    def get_misses(self) -> int:
        return len(self.goal_chain) - self.get_successes()
    
    def get_streak(self) -> int:
        return
    
    def get_days_on_goal(self) -> int:
        return len(self.goal_chain)

    def summary(self) -> None:
        print("Goal Name: {}\n Current Goal Score: {}\n Amnesty Allowance: {}\n Current Amnesty: {}\n Total Success: {}\n Total Missed: {}\n Current Streak: {}\n Days on Goal: {}" \
        .format(self.goal_name, self.get_score(), self.get_amnesty(), self.get_used_amnesty(), self.get_successes(), self.get_misses(), self.get_streak(), self.get_days_on_goal()))
    
    def vis_goal(self) -> None:
        pass

class Profile:
    def __init__(self, name:str) -> None:
        self.name = name
        self.goals = {}

    def new_goal(self, goal_name:str) -> list:
        self.goals[goal_name] = Goal(self.name)

if __name__ == "__main__":
    print("hi")
    race_peterson = Profile("Race Peterson")
    race_peterson.new_goal("Sleep")
    for _ in range(10):
        race_peterson.goals["Sleep"].make_day()
    race_peterson.goals["Sleep"].summary()