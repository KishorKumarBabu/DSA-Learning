from collections import Counter
def frequency(l):
    counts = Counter(l)
    freq=list(counts.values())
    min_fre=min(freq)
    max_fre=max(freq)
    min_fre_lis=[num for num,freq in counts.items() if freq==min_fre]
    man_fre_lis=[num for num,freq in counts.items() if freq==max_fre]
    man_fre_lis.sort()
    min_fre_lis.sort()
    return(min_fre_lis,man_fre_lis)
frequency([13,12,11,13,14,13,7,11,13,14,12])
    