import string
import random

class Game:
    def __init__(self):
        self.grid = []
    def is_valid(self,mot):
        mot=list(mot)
        lng=len(mot)
        e=True
        if lng!=0:
            for i in mot:
                c=mot.count(i)
                m=self.grid.count(i)
                if c>m:
                    e=False
                    print("Incorect test")
                    break
                else:
                    e=True
        else:
            e=False
        return e
  