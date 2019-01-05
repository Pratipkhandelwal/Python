def score_words(words):
    score = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for word in words:
        num_vowels = 0
        match = str(word)
        for letter in range(0,len(match)):
            for vowel in range(0,len(vowels)):
                if(match[letter] == vowels[vowel]):
                    num_vowels += 1
                    
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))
