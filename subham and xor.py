import collections

def CountFreq(a):
    return collections.Counter(a)


if __name__=="__main__":
    n = int(input())
    a = list(map(int,input().split()))
    freq = CountFreq(a)

    val = 0
    for k,v in freq.items():
        if(v>=2):
            val = val + v//2


print(val)
            

    

