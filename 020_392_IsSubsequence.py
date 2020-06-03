"""
4 level solution:
1. Divide and Conquer with Greedy (从这个solution理解了greedy algorithm的奥义，但code有点傻逼 没必要自己写了）
2. Two-Pointer （简单 直接 清爽，也是我第一眼想到的方法，正常人都用这个）

按理说，solution到这就应该结束了，但解法撰写人把此题给升华了，增加了难度，此题改为多个source一个target，所以有了下面两个solutions:

3. Greedy Match with Character Indices Hashmap （有所帮助，自己写了一下）
4. Dynamic Programming （和Edit Distance这个hard题有关，但这个算法用在此题很僵硬而且complexity效果不好，仅了解。

   time   space
1. O(T)   O(T)
2. O(T)   O(1)
3. O(T+S*logT) (我觉得：其实这里的logT没有那么大，在letter分布均匀的情况比这个小多了） O(T)
4. O(S*T) O(S*T)
"""

# 2. Two pointers （myself):
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_ptr = 0
        t_ptr = 0

        if len(s) == 0:   # 这两个特殊情况真的是恶心人
            return True
        if len(t) == 0:
            return False

        while True:
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1
            t_ptr += 1

            if s_ptr == len(s):
                return True
            elif t_ptr == len(t):
                return False

# 2. Two pointers (LeetCode solution) 这样写代码特殊情况就不用单独考虑了
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        p_left = p_right = 0
        while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
            # move both pointers or just the right pointer
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1

        return p_left == LEFT_BOUND


# 3. Greedy Match with Character Indices Hashmap
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(t):
            letter_indices_table[letter].append(index)

        curr_index = -1
        for letter in s:
            if letter not in letter_indices_table:
                return False
            else:
                indices_list = letter_indices_table[letter]
                match_index = bisect.bisect_right(indices_list, curr_index)  # 1. 必须用bisect_right而不是left
                if match_index != len(indices_list):  # 2. !=
                    curr_index = indices_list[match_index]
                else:
                    return False
        return True


# 明确，这题，需要循环s string，每个loop里用二分法去查找想要的match_index
# 所以curr_index是for循环的(s string)的index, match_index是每个循环内部indices_list的index,不一样

# 1. 必须用"bisect_right"
# 如果s string有连续重复的字母，bisect_right可以推进，bisect_left就在这个字母的indices_list原地踏步了。
# 而且biset_right还有往前进一位的功能，促成了2.

# 2. 这里用!=解决了一切需要终止的情况。
# 有两种需要终止的情况，一类是curr_index=len(indices_list) 另一类curr_index>len(indices_list)
# 而这两种情况都会变为match_index == len(indices_list)
# 而且解释下为什么这两种情况都需要终止，>就不用说了，肯定超了，=其实也超了，=的时候必然是连续重复字母的情况，超了是因为这里bisect_right自带+1功能

# 明早起来清算一下。上面说的bisect_right自带+1功能有点抽象了哈，这里的代码的逻辑其实是用上一个curr_index去找下一个curr_index的match_index，
# 所以当遇到相同的match_index，当然不行，那不是自己找自己吗，所以bisect_right刚好遇到相同往后移动一位。

# 分析到这里我们发现，其实用bisect_left也是可以的，办法就是把代码的逻辑改为用上一个curr_index+1 去找下一个curr_index的match_index，其实这样
# 才更自然顺畅吧！因为我们就是要用 当前的curr_index去找其match_index。

# bisect_left version: (written by myself, submit succeeded)
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(t):
            letter_indices_table[letter].append(index)

        curr_index = -1
        for letter in s:
            if letter not in letter_indices_table:
                return False
            else:
                indices_list = letter_indices_table[letter]
                match_index = bisect.bisect_left(indices_list, curr_index)
                if match_index != len(indices_list):
                    curr_index = indices_list[match_index] + 1
                else:
                    return False
        return True


"""
Bisect 库介绍
是用来二分查找（插入）的

总的来说，bisect.bisect_left bisect.bisect_right 是用来查找的用的，返回的是一个index； bisect.insect_left bisect.insect_right
是用来插入新元素用的，无返回值，并且这时候print原数组已经是插入新元素之后的数组。 但！是！bisect_left bisect_right 查找指定元素时也是
假设我要插入这个指定元素，返回的index是加入我插入指定元素后 该元素的index(但实际上并未插入，原数组还是原数组）

https://blog.csdn.net/sinat_38682860/article/details/96438515?utm_medium=distribute.pc_relevant.none-task-blog-baidujs-2
"""

"""
4th level solution 摘录：
Generally speaking, the dynamic programming algorithms tend to be faster than other solutions, since it reuses the 
intermediate solutions rather than recalculating them. However, it is not the case here.
不是很懂啊，到底什么是DP啊，怎么利用的中间量。
"""

"""
语法 letter_indices_table = defaultdict(list)

用defaultdict是因为 collections.defaultdict可以返回默认值，当被访问键不存在时，可以实例化一个值作为默认值。它是使用一个类型来初始化的。
这个类型应该是指 每个value的类型，例如此例是list。

dd = defaultdict(list)
dd
Out[19]: defaultdict(list, {})

dd['foo']
Out[25]: []
dd
Out[26]: defaultdict(list, {'foo': []})

https://blog.csdn.net/brucewong0516/article/details/81065988
"""