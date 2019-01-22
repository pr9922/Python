import functools
import logging
import sys
from functools import wraps

def logcalls(prefix):
    @wraps(prefix)
    def dec(func):
        @wraps(func)
        def wrap(*args, **kwds):
            lst = []
            for x in args:
                if isinstance(x,str):

                    lst.append(repr(str(x)))
                    #if str.isalpha(x) and len(str(x))>0:           #IN THE RIGHT DIRECTION
                    #    lst.append("\'" + str(x)+ "\'")
                    #else:
                    #    lst.append(str(x))
                else:
                    lst.append((str(x)))
            argstring = ", ".join(lst)
            if "t" in argstring:
                argstring=argstring + ", "
            if(len(argstring) >0 ) and str.isalpha(argstring):
                argstring = "\'"+ argstring +"\', "
            
            #argstring = argstring + ", "
            #argstring=seperator.join(lst)

            keyString=""
            for y in kwds:
                argstring +=str(y) + '=' + str(kwds[y]) 

            print(prefix+ ":" , func.__name__ + "(" + str(argstring) +")", file=sys.stderr)
            retFunc = func(*args, **kwds)
            print(prefix+ ": " + func.__name__ + " -> " + str(retFunc), file=sys.stderr)
            #retFunc = func(*args, **kwds)
            
            return retFunc
        return wrap
    return dec
    
    #raise NotImplementedError

def module_test(mod):

    for x in mod.__dict__:
        if not mod:  ##if not a module
            import __main__
            mod= __main__
        if str(x).startswith("test"):
              if callable(mod.__dict__[x]):  ##can be called
                #try:
                #    print(x + ": PASS", file=stderr)
                #except Exception:
                #    print(x + ": FAIL", file = sys.stderr)
                try:
                    if(mod.__dict__[x]):
                        print(x + ": PASS",file = sys.stderr)
                    else:
                        print(x+": FAIL",file = sys.stderr)
                except Exception as e:  ##called in rare cases
                    print(x+": FAIL",e)
                                   
                print(mod.__dict__[x].__doc__, file =sys.stderr)      

    
    #raise NotImplementedError
    
