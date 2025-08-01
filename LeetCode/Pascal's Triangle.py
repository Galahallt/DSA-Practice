from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        if numRows > 0:
            ans.append([1])
        if numRows > 1:
            ans.append([1, 1])

        if numRows > 2:
            for i in range(3, numRows + 1):
                _temp = []
                for j in range(i):

                    if j == 0:
                        _temp.append(ans[i - 2][0])
                    elif j == i - 1:
                        _temp.append(ans[i - 2][j - 1])
                    else:
                        _temp.append(ans[i - 2][j] + ans[i - 2][j - 1])

                ans.append(_temp)

        return ans
