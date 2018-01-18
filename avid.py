import sys

t=int(input())

def calc(qnum):
    x=0
    sum=0
    while qnum:
        y=qnum%10
        qnum=int(qnum/10)
        sum+=y *(4 ** x )
        x+=1
    return sum


def print_ans(first, remcount):
    i=0
    while first[i]!=-1:
        sys.stdout.write(str(remcount[first[i]]))
        i+=1


def calc_rem_freq(decnum):
    first=[-1]*decnum
    flag=[0]*decnum
    remcount=[0]*decnum
    i=0
    x=1
    y=2
    while y<=decnum:
        remainder=decnum%y
        remcount[remainder]+=1

        if not flag[remainder]:
            flag[remainder]=1
            first[i]=remainder
            i+=1
        x+=1
        y=2**x
    print_ans(first,remcount)
    print()


while t:
    t=t-1
    ln=int(input())
    qnum=int(input())
    decnum=calc(qnum)
    calc_rem_freq(decnum)
