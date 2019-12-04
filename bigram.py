def canFind(bigram, word):
    count = 0
    b = 0
    e = 0
    for each in word:
        while b < len(bigram):
            if bigram[b] not in each:
                print(bigram[b])
                print(each)
                print("false")
                print()
            b = b + 1
        while e < len(word):
            if bigram[e] not in word[e]:
                print(bigram[e])
                print(word[e])
                print("false")
                print()

            e = e + 1
        
    #return True
            
    #print("false")
    #return False
        #return True
canFind(["at", "be", "th", "au"], ["beautiful", "the", "hat"]), 
#canFind(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]), 
#canFind(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]), 
#canFind(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"])