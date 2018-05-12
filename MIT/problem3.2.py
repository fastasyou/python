def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    for partition in partitions(set_):
        yield [list(elt) for elt in partition]

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    L_copy = L.copy()
    maxsum = 0
    maxseq = []
    while len(L_copy) > 0:
        sum1 = 0
        seq = []
        for j in range(len(L_copy)):
            sum1 += L_copy[j]
            seq.append(L_copy[j])
            if maxsum < sum1:
                maxsum = sum1
                maxseq = seq.copy()
        del L_copy[0]
    return maxsum

print(max_contig_sum([3, 4, -1, 5, -4]))
print(max_contig_sum([3, 4, -8, 15, -1, 2]))
