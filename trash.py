import bisect

L = [1,2,3,6,8,12,15]
x = 3

aaa = bisect.bisect_left(L,x)
bbb = bisect.bisect_right(L,x)
print(aaa)
print(bbb)
print(L)