
from typing import List

class Solution:

    def lengthOfLongestSubstring(self, s: str):
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

    def testLengthOfLongestSubstring(self):
        examples = {
            "abcabdc": 4,
            "aab": 2,
            "a": 1,
            "": 0
        }

        for input, expected_output in examples.items():
            print(f"Input: '{input}'")
            output = self.lengthOfLongestSubstring(input)
            if output != expected_output:
                print(f"Error: Expected Output={expected_output} != Output={output}\n")
            else:
                print(f"Output: {output}\n")
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        result = []
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str in groups.keys():
                 result[groups[sorted_str]].append(str) 
            else:
                groups[sorted_str] = len(groups)
                result.append([str]) 
        return result
    
    def testGroupAnagrams(self):
        examples = [
            {
                "input": ["eat","tea","tan","ate","nat","bat"],
                "output": [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']]
            },
        ]
        
        for example in examples:
            input = example["input"]
            expected_output = sorted(example["output"])
            print(f"Input: '{input}'")
            output = sorted(self.groupAnagrams(input))
            if output != expected_output:
                print(f"Error: Expected Output={expected_output} != Output={output}\n")
            else:
                print(f"Output: {output}\n")


if __name__ == '__main__':
    s = Solution()
    s.testLengthOfLongestSubstring()
    s.testGroupAnagrams()
    
