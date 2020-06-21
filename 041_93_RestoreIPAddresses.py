"""
1 solution:
1. Backtracking (DFS)
time  O(1)  space  O(1)
"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        segments = []
        res = []
        def backtracking(current_pos,dot):
            for next_pos in range(current_pos+1,min(len(s)-1,current_pos+4)):  # 好好想想这里为什么是len(s)-1吧，弟弟
                segment = s[current_pos+1:next_pos+1]
                if valid(segment):
                    segments.append(segment)
                    if dot-1 == 0:
                        update_res(next_pos)
                    else:
                        backtracking(next_pos,dot-1)
                    segments.pop()
        def update_res(current_pos):
            segment = s[current_pos+1:]
            if valid(segment):
                segments.append(segment)   # 别忘辽
                res.append('.'.join(segments))
                segments.pop()              # 别忘辽
        def valid(segment):
            return int(segment)<=255 if segment[0]!='0' else len(segment)==1  # Note int()<255, !='0'
        backtracking(-1,3)
        return res