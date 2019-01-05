import collections
from collections import Counter

# Driver program
if __name__ == "__main__":
        n = int(input())
        s = input()
        most_occur = (collections.Counter(s).most_common(1)[0])
        print(len(s) - (most_occur[1]))
         
