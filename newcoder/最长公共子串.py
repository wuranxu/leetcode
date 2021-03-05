def sub_array(a, b):
    result = ""
    dp = [['' for _ in range(len(b))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                if i == 0 or j == 0:
                    dp[i][j] = a[i]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + a[i]
                if len(dp[i][j]) > len(result):
                    result = dp[i][j]
    return result


if __name__ == "__main__":
    a = "dqwhjdwhef"
    b = "wdwwoqwhjddwhe"
    print(sub_array(a, b))
