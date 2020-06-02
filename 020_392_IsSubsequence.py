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