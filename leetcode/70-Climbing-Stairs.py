class Solution:
    def climbStairs(self, n: int, memo = {0: 0}) -> int:
        # possJumps = []

        # if n >= 2: possJumps = [1, 2]
        # elif n == 1: possJumps = [1]

        # for jump in possJumps:
        #     remainingSteps = n - jump
        #     steps += 1
        #     if remainingSteps in memo: return memo[remainingSteps]
        #     memo[remainingSteps] = self.climbStairs(remainingSteps) +  steps
        # return memo[n]

        one, two = 1, 1
        for i in range(n-1):
            one, two = one + two, one
        return one
