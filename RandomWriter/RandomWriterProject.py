from enum import Enum
import graph
import urllib
import urllib.request
import pickle
import random
import os
import string
import sys
import tempfile
import collections


Tokenization=Enum('Tokenization','word character byte none')  ##Enum for token types

class RandomWriter(object):
    """A Markov chain based random data generator.
    """

    def __init__(self, level, tokenization=Tokenization.none, graph=None):
        
        self.currentMode = tokenization
        self.currentLevel = level
        
    def generate(self):
        
        if self.graph != None: ##yield random tokens if graph is not empty
            while True:
                yield self.graph.randomVal()  ##return generator
        else:
            print("Graph has not been initialized!")

    def generate_file(self, filename, amount):
        
        try:     
            if self.currentMode == Tokenization.byte:  ##if byte token, write tokens 
                self.genHelpByte(filename, amount)       
            else: ##not byte 
                self.genHelpNotByte(filename,amount)
        except AttributeError:
            print("There has been an Attribute Error")
        finally:
            pass
        
    def genHelpByte(self, filename, amount):
        
        if hasattr(filename,'write') and self.currentMode==Tokenization.byte:
            curr=self.generate()
            for x in range(amount):
                filename.write(bytes(next(curr)))

    def genHelpNotByte(self, filename, amount):
        
        if hasattr(filename, 'write'):
            for i in range(amount):
                curr = str(next(self.generate()))
                if self.currentMode is Tokenization.character:
                    pass
                else:
                    curr = curr + " "
                filename.write(curr)
                    
        else:  ##if no write option, then open a new file and write
            with open(filename, mode="w") as fi:
                self.generate_file(fi,amount)
    
    def save_pickle(self, filename_or_file_object):
        
        try:
            self.pickleHelp(filename_or_file_object)
        except AttributeError:
            print("There has been an attribute error")
            pass

    def pickleHelp(self, filename_or_file_object):
        
        if hasattr(filename_or_file_object, 'write'): ##if writable, dump
            pickle.dump(self, filename_or_file_object,pickle.HIGHEST_PROTOCOL)
        elif not hasattr(filename_or_file_object, 'write'): ##not writable, new file and save 
            with open(filename_or_file_object, "wb") as fi:
                self.save_pickle(fi)
    
    @classmethod
    def load_pickle(cls, filename_or_file_object):
        
        current = None
        try:
            current = pickle.load(filename_or_file_object)
            if isinstance(current, cls):
                return current
        except:
            with open(filename_or_file_object, "rb") as fi:
                current = pickle.load(fi)
                return current

        else:
            return None    
        finally:
            pass

        return current

    def train_url(self, url):
        
        curr = urllib.request.urlopen(url)
        currRead=curr.read()
        if self.currentMode != Tokenization.none:     
            if self.currentMode == Tokenization.byte:
                pass       
            else:
                currRead = str(currRead,encoding="utf-8")
        self.train_iterable(currRead)

    def urlHelp(self, currRead):
        if self.currentMode == Tokenization.byte:
            pass       
        else:
            currRead = str(currRead,encoding="utf-8")
            return currRead


    def train_iterable(self, data):

        self.graph=graph.Graph()  ##initialize attribute
        try:
            if isinstance(data,str):   ##Checks currentMode and adjusts data accordingly
                if self.currentMode == Tokenization.word:
                    data = data.split()
                elif self.currentMode == Tokenization.character:
                    pass
            else:
                if self.currentMode == Tokenization.byte:
                    if isinstance(data, bytes):
                        pass
                if self.currentMode == Tokenization.none:
                    if hasattr(data,'__iter__'):
                        pass
                    else:
                        data = None         
            
            if self.currentLevel == 0:
                for i in range(len(data)):
                    curr =tuple(data[i:i+1])
                    self.graph.append(curr)
            else:
                if isinstance(data, collections.Iterable):
                    temp = []                   
                    for i in data:    
                        temp.append(i)     
                    data=temp
            for i in range(len(data)-self.currentLevel +1):
                curr = tuple(data[i:i+self.currentLevel])
                self.graph.append(curr)

        except TypeError: 
            raise TypeError
            pass

