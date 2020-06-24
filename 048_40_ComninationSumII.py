"""
1 solution:
1. Backtracking
"""
# solution 1 base (time score 36%) 经典combination backtracking
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(first=0,curr=[]):
            if sum(curr) == target:
                res.append(curr[:])
                return
            if sum(curr) > target:
                return
            for i in range(first,len(candidates)):
                if candidates[i] == candidates[i-1] and i-1>=first: # 我差点儿自己都不知道为什么自己写的code可行
                    continue
                curr.append(candidates[i])
                backtrack(i+1,curr)
                curr.pop()
        candidates.sort()
        res = []
        backtrack()
        return res

# solution 1 (time score 优化到90%以上）
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(first=0,curr=[],target=target):
            if target==0:
                res.append(curr[:])
                return
            for i in range(first,len(candidates)):
                if candidates[i] > target: # 这个break 而不是continue (time score 80%) 或者在上面判断target<0 (time score 55%)，让time score提高到90%以上
                    break                  # 还有这个实测，这个if放在下一个if前面，很重要。不然time score 变为70%。想去吧弟弟。# 哎 我不扣细节了
                if candidates[i] == candidates[i-1] and i-1>=first:
                    continue
                curr.append(candidates[i])
                backtrack(i+1,curr,target-candidates[i]) # 这里每步都减去，而不是上面sum判断，让time score从中下变为中上。
                curr.pop()
        candidates.sort()
        res = []
        backtrack()
        return res