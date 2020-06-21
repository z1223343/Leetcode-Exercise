"""
1 solution:
1. Backtracking (实际上没有backtracking...)

1. time  O(3**N * 4**M)   space  O(3**N * 4**M)
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']}
        def backtracking(combinations, next_digits):
            if not next_digits:
                output.append(combinations)  # 我的意思是这里改为return combinations
            else:
                for letter in phone[next_digits[0]]:
                    backtracking(combinations+letter,next_digits[1:])
        output = []
        if digits:
            backtracking('',digits)
        return output

"""
一个有意思的事,要是让func backtracking 一个一个return combinations，然后在主程序 ans = backtracking('',digits)会得到一个[].
"""