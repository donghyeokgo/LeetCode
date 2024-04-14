# 49 Group Anagrams
import collections
from typing import List, DefaultDict

strs = ["eat","tea","tan","ate","nat","bat"]
def groupAnagrams1(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()


