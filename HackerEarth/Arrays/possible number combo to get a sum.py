def C(n, step, cnt, v, m):
    if cnt > n or step > n:
        return
    if cnt == n and len(v)==m:
        # if counter cnt reached n print the list
        print(*v)
    else:
        # else append the step size to list
        v.append(step)
        # increment the cnt by step and recurse
        C(n, step, cnt + step, v,m)
        # remove the last step item from list
        v.pop()
        # increment the step size and recurse
        C(n, step + 1, cnt, v,m)


if __name__=="__main__":
    n,m = map(int,input().split())
    z = list()
    a = list()
    arr2d = [[j for j in input().strip()] for i in range(n)] 
    C(m, 1, 0, [], n)
    
