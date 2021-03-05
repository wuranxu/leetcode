from typing import List


# 本来差点忍不住要看答案了，但是想着毕竟是简单题 就不要想太复杂了吧
# 题目说的是每次让(n-1)个数字+1, 其实换个角度的话，就是让一个数字减去1.
#
# 一个数字减1，要所有数字都相等，所以我们可以先找到最小的那个数字为min_value，
#
# 然后遍历数组, 计算出每个数减1到min_value的次数，最后返回总和就好了~

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_value = min(nums)
        total = 0
        for n in nums:
            if n > min_value:
                total += n - min_value
        return total
