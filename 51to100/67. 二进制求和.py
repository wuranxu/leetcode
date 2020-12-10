class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        # 补全少的一方，以免循环结束后继续判断
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        elif len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        i, j = len(a) - 1, len(b) - 1
        flag = False
        while i >= 0 and j >= 0:
            if a[i] == "1" and b[j] == "1":
                if flag:
                    result = "1" + result
                else:
                    result = "0" + result
                flag = True
            elif a[i] == '0' and b[j] == '1' or a[i] == '1' and b[j] == '0':
                if flag:
                    result = "0" + result
                else:
                    result = "1" + result
            else:
                if flag:
                    result = "1" + result
                    flag = False
                else:
                    result = "0" + result
            i -= 1
            j -= 1
        if flag:
            return "1" + result
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary("101001", "1111"))
