from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        # 建立映射关系
        dct = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        # 结果数组
        ans = []

        def dfs(start, data):
            if start == len(digits):
                ans.append(data)
                return
            for d in dct[digits[start]]:
                data += d
                dfs(start + 1, data)
                data = data[:len(data) - 1]

        dfs(0, "")
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("24"))
