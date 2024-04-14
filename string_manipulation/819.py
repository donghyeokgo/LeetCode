# 819 Most Common Word

import collections
import re
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split() if word not in banned]

    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    max_count = 0
    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            max_count_word = word

    return max_count_word

# use Counter

def mostCommonWord2(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
             if word not in banned]

    counts = collections.Counter(words)


    return (counts.most_common(1)[0][0])
