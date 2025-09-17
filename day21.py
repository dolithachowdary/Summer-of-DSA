"""
Day 21: LeetCode Daily Challenge Problems
-----------------------------------------

✅ Problems Covered:
1. Replace Words
2. Top K Frequent Words
3. Sort Characters By Frequency
4. Group Anagrams
5. Longest Palindrome
6. Word Break
"""

from typing import List
from collections import Counter, defaultdict
import heapq


"""
Problem 1: 648. Replace Words (Medium)
--------------------------------------
Replace successors in sentence with shortest root from dictionary.
"""
class Solution1:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)  # sort roots by length
        words = sentence.split()
        for i, word in enumerate(words):
            for root in dictionary:
                if word.startswith(root):
                    words[i] = root
                    break
        return " ".join(words)

# Time: O(N*M) | Space: O(N+M)


"""
Problem 2: 692. Top K Frequent Words (Medium)
---------------------------------------------
Find k most frequent words, sort by frequency and lex order.
"""
class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

# Time: O(N log N) | Space: O(N)


"""
Problem 3: 451. Sort Characters By Frequency (Medium)
-----------------------------------------------------
Sort string by frequency of characters.
"""
class Solution3:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_chars = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        return "".join([ch * freq for ch, freq in sorted_chars])

# Time: O(N log N) | Space: O(N)


"""
Problem 4: 49. Group Anagrams (Medium)
---------------------------------------
Group words that are anagrams of each other.
"""
class Solution4:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))  # sorting characters
            groups[key].append(word)
        return list(groups.values())

# Time: O(N*K log K) | Space: O(N*K)  (K = max word length)


"""
Problem 5: 409. Longest Palindrome (Easy)
-----------------------------------------
Return length of longest palindrome that can be built from given string.
"""
class Solution5:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        odd_found = False
        for freq in count.values():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                odd_found = True
        return length + 1 if odd_found else length

# Time: O(N) | Space: O(1)


"""
Problem 6: 139. Word Break (Medium)
-----------------------------------
Given a string s and a dictionary of words, determine if s can be segmented into a space-separated sequence of dictionary words.
"""
class Solution6:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]

# Time: O(N^2) | Space: O(N)

