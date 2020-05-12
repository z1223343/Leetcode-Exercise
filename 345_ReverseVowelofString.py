"""
Two pointers.

Also has other options in: https://blog.csdn.net/qq_34364995/article/details/80715449?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158908514019724845021185%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=158908514019724845021185&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_v2~rank_v25-2-80715449.nonecase&utm_term=leetcode+345+python
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        slist = list(s)
        result = [None] * len(list(s))
        i = 0
        j = len(slist) - 1
        while i <= j:
            if slist[i] not in vowels:
                result[i] = slist[i]
                i += 1
            elif slist[j] not in vowels:
                result[j] = slist[j]
                j -= 1
            else:
                result[i] = slist[j]
                result[j] = slist[i]
                i += 1
                j -= 1
        return ''.join(result)


"""
''.join(a):  is to create a string using list 'a', if want to use comma to separate the elements, use ','.join(a)

a = [None] * len: is a way to initialize a known-length list. If the length is unknown, use a.append()

slist = list(s): to convert a string to a list.

Note in the solution "i<=j". must have '=' to cover all elements.

"""