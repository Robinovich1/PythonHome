class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] will store the number of unique BSTs that can be formed with i nodes
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1  # base cases: 1 way to form a BST with 0 or 1 nodes

        # Fill the dp array for all numbers of nodes from 2 to n
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        # The answer for n nodes is stored in dp[n]
        return dp[n]
