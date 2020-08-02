"""
3 level solution:
1. sort + find median
2. without finding median
3. quick sort (optimal solution)

    time      space
1.  O(nlogn)  O(1)
2.  O(nlogn)  O(1)
3.  O(n)      O(1)
"""

# solution 1:
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        sum = 0
        for num in nums:
            sum += abs(nums[len(nums)//2]-num)
        return sum
# wc, 我提交的时候没有注意到sum是python预定义的变量名，但是也没有bug。可以用啊

# solution 2：
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        sum = 0
        nums.sort()
        while l<r:
            sum += nums[r]-nums[l]
            l+=1
            r-=1
        return sum

# solution 3: 复习了quick selection，我无敌了
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def partition(start, end):
            pivot = random.randint(start, end)
            nums[start], nums[pivot] = nums[pivot], nums[start]
            left = start
            right = end

            while left < right:
                while nums[right] > nums[start] and left < right:  # 注意right先循环left
                    right -= 1
                while nums[left] <= nums[start] and left < right:  # note <=
                    left += 1
                nums[left], nums[right] = nums[right], nums[left]

            nums[start], nums[left] = nums[left], nums[start]  # 一定要记得换过来
            return left

        start = 0
        end = len(nums) - 1
        res_sum = 0
        while start <= end:  # 要<=
            k = partition(start, end)
            if k == len(nums) // 2:  # 进入改题目主题
                for num in nums:
                    res_sum += abs(num - nums[k])
                return res_sum
            elif k < len(nums) // 2:
                start = k + 1  # 可以+1
            else:
                end = k - 1  # 可以-1

