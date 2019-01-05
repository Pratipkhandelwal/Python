from collections import Counter

def find_most_occ_char(input):

	wc = Counter(input)

	s = max(wc.values())
	i = wc.values().index(s)
	
	print(wc.items()[i])

# Driver program
if __name__ == "__main__":
	input = 'aaaaa'
	find_most_occ_char(input)
