def load_dna(filename):
    
    with open(filename) as dna:
        while True:
            ch = dna.read(1)
            if ch:
                if 'A' <= ch <= 'Z':
                    yield ch
            else:
                break

    


def complement_dna(strand):
    
    for x in strand:
        y=x
        if x=="A":
            y="T"
        elif x=="T":
            y="A"
        elif x=="G":
            y="C"
        elif x=="C":
            y="G"
        yield y
        

    
    #raise NotImplementedError

def save_dna(strand, filename):

    with open(filename,'w') as res:
        for letter in strand:
            res.write(letter)
        
