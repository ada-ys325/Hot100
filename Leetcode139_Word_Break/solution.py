class Solution: 
  def wordBreak(self, s:str, wordDict: list[str])-> bool:
    word_set = set(wordDict)
    n = len(s)
    
    dp = [True]+ [False]*n 

    for i in range(1,n+1): 
      dp[i] = any(dp[j] and s[j:i] in word_set for j in range(i))
    
    return dp[n]