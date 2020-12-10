from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 由于找零只关心5块和10块的数量，并不关心20的数量，所以只定义2个变量
        # 分别是f表示还有多少5块钱，t表示还有多少10块钱
        f, t = 0, 0
        for b in bills:
            if b == 5:
                # 如果是5块，直接+1，因为不需要找零
                f += 1
            elif b == 10:
                # 来了张10块 没有5块找，直接return False(找不开)
                if f == 0:
                    return False
                # 否则5块-1 10块+1
                f -= 1
                t += 1
            else:
                # 没有10块直接找3个5块，如果没有3个5块，说明找不开
                if t == 0:
                    if f < 3:
                        return False
                    f -= 3
                else:
                    t -= 1
                    # 有10块没有5块，也直接算找不开
                    if f == 0:
                        return False
                    f -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.lemonadeChange([5, 5, 10, 5, 10, 5, 10, 20, 5, 5, 5, 20]))
