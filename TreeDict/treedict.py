import binarysearchtree
import collections
from binarysearchtree import Node
import itertools


class TreeDict(object):
    
    def __init__(self, args=None, **kwds): ##Default Constructor, creates new node and updates       
        self.rootNode = Node()
        self.update(args, **kwds)

    def __getitem__(self, key):  ##acts as the TreeDict[i] 
        if key is None:
            raise KeyError
        else:    
            try:   ##lookup in binarysearchtreeclass
                return self.rootNode.lookup(key).value
            except ValueError:
                raise KeyError
            

    def __setitem__(self, key, value):  ##used as the TreeDict[i]=blah     
        if key is None:
            raise KeyError
        try:
            return self.rootNode.insert(key, value)
        except ValueError:
            print("Value Error")    
            
  
    def __contains__(self, key): ##if blah in Treedict   
        if key is None:
            raise KeyError
        else:
            try:
                self.rootNode.lookup(key)  ##lookup and return true
                return True
            except ValueError:
                print("Value Error") 
                return False
    

    def get(self, key, default=None):   ##td.get 
        if key is None:
            raise KeyError
        else:       
            try:
                return self.rootNode.lookup(key).value
            except ValueError:
                return default
            

    def __delitem__(self, key): #
        if key is None:
            raise KeyError
        else:
            return self.rootNode.delete(key)
    

    
    def update(self, args, **kwds):
        if kwds:  
            for key, value in kwds.items():
                self.rootNode.insert(key, value)
        elif isinstance(args, dict):
            currDict = args
            for key in currDict.keys():
                self.rootNode.insert(key,currDict[key])
        elif isinstance(args, TreeDict):
            self.rootNode = args.rootNode
        elif isinstance(args, collections.Iterable):
            for pair in args:
                key,value = pair[0], pair[1]
                self.rootNode.insert(key, value)
        else:
            return None
                       

    def __len__(self):    
        nodes= self.iterate(self.rootNode)
        if self.rootNode.key == None or self.rootNode.value == None:
            return 0
            
        count = 0
        for node in nodes:
            count = count+1
        return count
    
    def iterate(self, currNode):
        if currNode.left != None:
            yield from self.iterate(currNode.left)
        yield currNode.key, currNode.value
        if currNode.right != None:
            yield from self.iterate(currNode.right)
            
    def __iter__(self):      
        for i, j in self.iterate(self.rootNode):
            yield i

    def items(self):   
        for i in self.iterate(self.rootNode):
            yield i

    def values(self):
        for v in self.iterate(self.rootNode):
            yield v,k
        
