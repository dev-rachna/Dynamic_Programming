# -*- coding: utf-8 -*-

'''
leetcode 72. Edit Distance
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character
'''


def minDistance(word1, word2):
    
    dp=[[0 for i in range(len(word2)+1)] for _ in range(len(word1)+1)]
    # print(dp)
    #base cases
    for i in range(len(word2)+1):
        dp[0][i]=i       
    for i in range(len(word1)+1):
        dp[i][0]=i
    
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            
            if word1[i-1]==word2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    
    print(dp[-1][-1])


minDistance("intention","execution")