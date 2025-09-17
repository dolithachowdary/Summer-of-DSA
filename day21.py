"""
Day 21: LeetCode Daily Challenge Problems
-----------------------------------------

Problem 1: 648. Replace Words (Medium)
--------------------------------------
In English, we have a concept called root, which can be followed by some words to form another longer word - let's call this word successor. 
For example, the root "cat" can be followed by "er" to form "cater". 

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, 
replace all the successors in the sentence with the root forming it. 
If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
"""

from typing import List

class Solution1:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)  # shortest roots first
        words = sentence.split()
        for i, word in enumerate(words):
            for root in dictionary:
                if word.startswith(root):
                    words[i] = root
                    break
        return " ".join(words)

# Dry Run:
# dictionary = ["cat", "bat", "rat"], sentence = "the cattle was rattled by the battery"
# → "the cat was rat by the bat"

# Time: O(N*M)  |  Space: O(N+M)


"""
Problem 2: 692. Top K Frequent Words (Medium)
---------------------------------------------
Given an array of strings words and an integer k, return the k most frequent strings.
The answer should be sorted by frequency from highest to lowest. 
Sort the words with the same frequency by their lexicographical order.

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
"""

import heapq
from collections import Counter

class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

# Dry Run:
# words = ["i","love","leetcode","i","love","coding"], k=2
# count = {"i":2,"love":2,"leetcode":1,"coding":1}
# heap = [(-2,"i"),(-2,"love"),(-1,"leetcode"),(-1,"coding")]
# → ["i","love"]

# Time: O(N log N)  |  Space: O(N)


"""
Problem 3: 451. Sort Characters By Frequency (Medium)
-----------------------------------------------------
Given a string s, sort it in decreasing order based on the frequency of the characters. 

Input: s = "tree"
Output: "eert"
"""

class Solution3:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_chars = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        return "".join([ch * freq for ch, freq in sorted_chars])

# Dry Run:
# s = "tree"
# count = {"t":1,"r":1,"e":2}
# sorted → [("e",2),("r",1),("t",1)]
# → "eert"

# Time: O(N log N)  |  Space: O(N)


"""
Problem 4: 49. Group Anagrams (Medium)
---------------------------------------
Given an array of strings strs, group the anagrams together.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
"""

from collections import defaultdict

class Solution4:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)
        return list(groups.values())

# Dry Run:
# strs = ["eat","tea","tan","ate","nat","bat"]
# "aet" → ["eat","tea","ate"], "ant" → ["tan","nat"], "abt" → ["bat"]
# → [["eat","tea","ate"],["tan","nat"],["bat"]]

# Time: O(N*K log K)  |  Space: O(N*K)  (K = max word length)

