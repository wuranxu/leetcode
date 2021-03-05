from typing import List


# 方法一
# 首先排序的思路大家都知道了，先排序然后遍历看是否是等差的。
#
# 这也是我的第一反应，但是我觉得这肯定不是最优解。
# 方法二
# 我们想一下，先遍历，找出最小的2个数字，first和second。
#
# 先假设他是等差数列，那么他们之间的差sub，通过一次遍历就可以拿到了。
#
# 然后在第一次遍历的时候，我们可以把所有数字都存放到Map或者Set之中。
#
# 然后开始第二次遍历，通过sub可以计算出等差数列的第三个数，
#
# 判断它在不在刚才的Map/Set中即可，如果不在，直接return False, 最后return True
# 注意点
# 还有2个地方需要注意:
#
# 如果求出来的sub是0该怎么办，很简单，是0的话如果它是等差数列，那么set的长度不会超过1
#
# 如果数字有重复怎么办，很简单，有重复的话，会走到not in set逻辑导致直接return False
#
# 有的同学可能觉得not in set是O(n)的操作，这里不做解释(其实不知道怎么解释好)~


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        nums = set()
        first, second = float("inf"), float("inf")
        for n in arr:
            if n < second:
                if n < first:
                    second = first
                    first = n
                else:
                    second = n
            nums.add(n)
        sub = second - first
        if sub == 0 and len(nums) > 1:
            return False
        for i in range(len(arr)):
            if first + sub * i not in nums:
                return False
        return True
