from django.db import models
import random, datetime

class logSheet:
    def __init__(self):
        self.activitiesDict = []
        self.logNumber = 0
        self.gold = 0

    def clear(self):
        self.activitiesDict = []
        self.logNumber = 0
        self.gold = 0
        return self        

ledger = logSheet()

class workplace:
    def __init__(self, name, floor, ceiling):
        self.name = name
        self.floor = floor
        self.ceiling = ceiling
        self.wallet = 0
        self.color = ''
        self.ledger = ''

    def earnGold(self):
        goldRand = random.randint(self.floor, self.ceiling)
        self.wallet += goldRand

        return self.wallet    

    def log(self):
        if self.wallet < 0:
            ledger.activitiesDict.append('<li style="color: red;">Lost %s gold from the %s  %s </li>' %(self.wallet, self.name, datetime.datetime.now()))
            self.color = 'red'
        else:
            ledger.activitiesDict.append('<li style="color: green;">Earned %s gold from the %s  %s </li>' %(self.wallet, self.name, datetime.datetime.now()))
            self.color = 'green'
        ledger.logNumber += 1        
        return self

    def endGame(self):
        if ledger.gold > 490:
            ledger.activitiesDict.append('<li style="color: purple;">Winner! %s  %s </li>' %(ledger.gold, datetime.datetime.now()))
            self.color = 'purple'

        if ledger.logNumber > 15:
            ledger.activitiesDict.append('<li style="color: yellow;">No more moves! %s </li>' %(datetime.datetime.now()))
            self.color = 'yellow'
        return self