"""
Day 21: LeetCode Daily Challenge
Problem: 648. Replace Words (Medium)

Description:
------------
In English, we have a concept called root, which can be followed by some words to form another longer word - let's call this word successor. 
For example, the root "cat" can be followed by "er" to form "cater". 

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, 
replace all the successors in the sentence with the root forming it. 
If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

Example:
--------
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Constraints:
------------
- 1 <= dictionary.length <= 1000
- 1 <= dictionary[i].length <= 100
- 1 <= sentence.length <= 10^6
- sentence consists of lowercase English letters and spaces.
- The roots in dictionary are distinct.
"""

from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Sort roots by length to ensure smallest root replaces first
        dictionary.sort(key=len)
        dictionary_set = set(dictionary)

        words = sentence.split()
        for i, word in enumerate(words):
            for root in dictionary:
                if word.startswith(root):
                    words[i] = root
                    break
        return " ".join(words)


# -----------------------
# Dry Run
# -----------------------
# dictionary = ["cat", "bat", "rat"], sentence = "the cattle was rattled by the battery"
# words = ["the", "cattle", "was", "rattled", "by", "the", "battery"]
# For "cattle": starts with "cat" → replace → "cat"
# For "rattled": starts with "rat" → replace → "rat"
# For "battery": starts with "bat" → replace → "bat"
# Final: "the cat was rat by the bat"

# -----------------------
# Time and Space Complexity
# -----------------------
# Time Complexity: O(N * M) 
#   - N = number of words in sentence
#   - M = number of roots in dictionary
#   - Each word is checked against roots
#
# Space Complexity: O(N + M) 
#   - For storing words list and dictionary set
