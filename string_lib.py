
def lengthOfLongestSubstring(s: str):
    charSet = ""
    maxLen = 0
    for c in s:
        if c not in charSet:
            charSet += c
            maxLen = max(maxLen, len(charSet))
        else:
            while c in charSet:
                charSet = charSet[1:]
            charSet += c
        print(f"current best: '{charSet}'")
    return maxLen

if __name__ == '__main__':

    examples = [
        "abcabdc",
        "aab",
        "a",
        ""
    ]

    for ex in examples:
        print(f"Input: '{ex}'")
        print(f"Output: {lengthOfLongestSubstring(ex)}\n")