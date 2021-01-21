'''
377. Combination Sum IV
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

'''

def combinationSum4(nums, target):

    dp=[0 for i in range((target)+1)]
    dp[0]=1
    for i in range(1,target+1):
        for j in nums:
            if i>=j:
                dp[i]=dp[i]+dp[i-j]
    
    return dp[-1]


print(combinationSum4([1, 2, 3],4))