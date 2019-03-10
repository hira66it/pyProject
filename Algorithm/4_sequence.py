import copy
def almostIncreasingSequence(sequence):
    test_pass = False
    for i in range(len(sequence)):
        tmp_seq = copy.deepcopy(sequence)
        
        del tmp_seq[i]
        tmp_seq=sorted(tmp_seq)
        if sum(tmp_seq) == tmp_seq[-1]*(2*tmp_seq[-1]-len(sequence)+2)/2:
            test_pass = True
    return test_pass
print(almostIncreasingSequence([10, 1, 2, 3, 4, 5]))