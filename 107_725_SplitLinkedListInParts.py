"""


"""


# solution 1: (这个解法两个连续赋值给我看懵逼了，看了两天也没彻底看懂。。，很不友好）

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        cur = root
        for N in range(1001):
            if not cur:
                break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = write = ListNode(None) # 第一个连续赋值
            for j in range(width + (i < remainder)):
                write.next = write = ListNode(cur.val)  # 第二个连续赋值
                if cur:
                    cur = cur.next
            ans.append(head.next)
        return ans

# 后来我自己改写了以下代码，可以成功运行，区别是第二个连续赋值分开连个赋值写，这样更容易和理解，算是明白一些了：
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        cur = root
        for N in range(1001):
            if not cur:
                break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = write = ListNode(None)
            for j in range(width + (i < remainder)):
                write.next = ListNode(cur.val)
                write = write.next
                if cur:
                    cur = cur.next
            ans.append(head.next)
        return ans


# solution 2:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        cur = root
        for N in range(1001):
            if not cur:
                break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in range(k):
            head = cur
            for j in range(width + (i < remainder) - 1):
                if cur:
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next  # 这个赋值也有点骚，但总体比solution1好理解，但结构挺巧妙，solution1结构思路更直接
            ans.append(head)
        return ans


# 总结：
# head = write = listNode(None) 这个连续赋值这是说，head和cur同时指向一个内存，这个内存包含一个listNode(None)，所以理论上说我们改这个内存的值，head和cur会同时变。改cur，head也会变，比如让cur.next = 2，head.next也会 = 2.

# write = write.next  只是cur往下移一位，和head无关，head不变不移位

# write.next = write = ListNode(cur.val) 这个可以写成
# write.next = ListNode(cur.val)
# write = write.next
# 第一步因为我们赋值了write.next，所以也会赋值head.next 即head的下一位。
# 第二步是write向下移一位,这个又和head无关，但影响是write向下移了一位，在下个循环里write.next就是head.next.next了。

# cur.next,cur = None,cur.next 这里参考下面的连续赋值csdn帖子，第一个赋值cur.next是为了改head,第二个赋值cur是为了进入下一个循环。

# write.next = write 这个句子单独写会报错的啊，会显示链表循环了。



"""
note: in python3, there is no xrange()

about assignment(赋值) in Python （尤其是连续赋值问题） 见：
https://blog.csdn.net/xjcvip007/article/details/54348245


"""