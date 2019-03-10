def almostIncreasingSequence(sequence):
    seq = sequence
    i=0
    tmp =0
    while i<len(seq)-1:
        if not seq[i] < seq[i+1]:
            if len(seq)-i >3:
                if not (seq[i] < seq[i+2] and seq[i+2] < seq[i+3]):
                    tmp +=1
                    i+=3
            elif len(seq)-i>2:
                if not (seq[i] < seq[i+2]):
                    tmp +=1
                    i+=2
            else:
                tmp+=1
                i+=1
        i+=1
        if tmp>1:return False
    return True
print( almostIncreasingSequence([]))