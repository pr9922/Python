import sys
import collections
from collections import Counter
import random
import final
import os



class Graph():
    
    def __init__(self, curr=None):
        self.grid={curr:Counter()}
        self.key = curr

    def append(self, isNext):
        try:
            self.appendCheck(isNext)
        except ValueError:
            print("There is a value error!")

    def appendCheck(self,isNext):
        if self.key != None:
            if isNext not in self.grid:
                self.grid[isNext] = Counter()
            self.gridUpdate(isNext)    
        elif self.key == None:
            self.__init__(isNext)
            pass
        
    def gridUpdate(self,isNext):
        self.grid[self.key][isNext] += 1
        self.key = isNext 
           
    def addNext(self):
        
        currCount = 0
        for i in self.grid[self.key].values():
            currCount+=i
            
        currVal = random.randint(1, currCount)
        
        try:    
            return self.addNextHelp(currVal)
        except IndexError:
            print("There has been an error with indexing dude")
            pass

        
    def addNextHelp(self, currVal):
        for x,y in self.grid[self.key].items():
            currVal = currVal - y
            if currVal <= 0:
                return x
            else:
                pass
        
                       
    def randomVal(self):
        try:
            self.key = self.addNext()
        except:
            self.key = random.choice(list(self.grid))
        finally:
            return self.key[-1]

    
