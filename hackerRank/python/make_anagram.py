#!/bin/python3

# Problem Statement:
# Given a single string `s` of length N, split it into two halves:
#   - s1 = s[:N // 2]
#   - s2 = s[N // 2:]
# 
# Transform `s1` so that it becomes an anagram of `s2` by replacing duplicate
# characters in `s1` (characters whose count exceeds their frequency in `s2`)
# with characters that appear more frequently in `s2` than in `s1`.
# Finally, output both the transformed `s1` and `s2` separated by a single space.
# 
# Constraints:
# - 2 <= len(s) <= 10^5 (or any even/odd string length; if len(s) is odd, the
#   middle character is excluded from s1 because mid = len(s) // 2)
# - `s` consists of printable non-whitespace characters (e.g., ASCII digits or letters)
# 
# Sample Input:
# 121123
# 
# Sample Output:
# 123 123
# 
# Explanation:
# - Input string `s` = "121123" (length 6, mid = 3)
# - `s1` = "121", `s2` = "123"
# - In `s1`, `'1'` appears twice, while `s2` only needs `'1'` once and is missing `'3'`.
# - Scanning `s1`, the second `'1'` exceeds `c2['1']` and is replaced with `'3'`,
#   turning `s1` into "123".
# - The function returns `"123 123"`.

# python3 make_anagram.py

from collections import Counter

def make_anagram_prefer_remove(s1: str, s2: str) -> str:
    c1 = Counter(s1)
    c2 = Counter(s2)

    # Characters missing in s1 compared to s2
    missing = []
    for ch, freq in c2.items():
        if freq > c1[ch]:
            missing.extend([ch] * (freq - c1[ch]))

    chars = list(s1)
    seen = Counter()

    # First pass: replace duplicate characters that exceed target count
    for i, ch in enumerate(chars):
        seen[ch] += 1
        if seen[ch] > c2[ch] and missing:
            chars[i] = missing.pop()

    return "".join(chars) + " " + s2

if __name__ == '__main__':
    s = input().strip()
    mid = len(s) // 2
    print(make_anagram_prefer_remove(s[:mid], s[mid:]))
