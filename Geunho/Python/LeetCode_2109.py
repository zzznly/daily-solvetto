# https://leetcode.com/problems/adding-spaces-to-a-string/
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = []
        spaces = set(spaces)
        for index, char in enumerate(s):
            if index in spaces:
                answer.append(f' {char}')
            else:
                answer.append(char)

        return ''.join(answer)


s = Solution()
assert s.addSpaces('l', [0]) == ' l'
assert s.addSpaces('LeetcodeHelpsMeLearn', [8, 13, 15]) == 'Leetcode Helps Me Learn'
assert s.addSpaces('icodeinpython', [1, 5, 7, 9]) == 'i code in py thon'
assert s.addSpaces('spacing', [0, 1, 2, 3, 4, 5, 6]) == ' s p a c i n g'
