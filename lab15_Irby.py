#Adam Irby
#CST 205 Lab 15
#=-=-=-=-=-=-=-=
import random


class dice:
  numOfDice = None
  sidesOfDie = None
  rolls = []
  
  def __init__(self, numOfDice, sidesOfDie):
    self.sidesOfDie = sidesOfDie
    self.numOfDice = numOfDice
    
    for i in range(0, numOfDice):
      self.rolls.append(random.randrange(self.sidesOfDie))
      
  def rollAllDice(self):
    for i in range(0, self.numOfDice):
      self.rolls[i] = random.randrange(self.sidesOfDie)
      
  def rollSingleDie(self, dieToRoll):
    if dieToRoll < len(self.rolls):
      self.rolls[dieToRoll] = random.randrange(self.sidesOfDie)
      
  def getRolls(self):
    return self.rolls
   
  def test(self):
    pass