def insertion(seq):
    for i in range(len(seq)):
        pos=i
        for j in range(i,):
            if seq[pos] < seq[pos-1]:
                seq[pos],seq[pos-1]=seq[pos-1],seq[pos]
                pos=pos-1
    print(seq)
seq=list(range(5000,1,-1))
insertion(seq)