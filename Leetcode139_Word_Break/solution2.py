from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        使用动态规划解决单词拆分问题
        """
        # 为了快速查找，将列表转换为哈希集合
        # O(m) 的时间复杂度，m 是字典中单词的数量
        word_set = set(wordDict)
        
        # dp[i] 表示 s 的前 i 个字符 s[0..i-1] 是否可以被拆分
        # 数组长度为 len(s) + 1
        dp = [False] * (len(s) + 1)
        
        # 基础情况：空字符串总是可以被拆分的
        dp[0] = True
        
        # i 代表字符串的长度，从 1 到 len(s)
        for i in range(1, len(s) + 1):
            # j 是分割点，将 s[0..i-1] 分为 s[0..j-1] 和 s[j..i-1]
            for j in range(i):
                # 如果 dp[j] 是 true (即 s[0..j-1] 可拆分)
                # 并且 s[j..i-1] 这个子串在字典里
                # 那么 dp[i] 就可以被设置为 true
                # s[j:i] 在 Python 中就是截取索引 j 到 i-1 的子串
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    # 既然已经找到一种拆分方法，就无需再为 dp[i] 寻找其他方法了
                    # 直接跳出内层循环，去计算下一个 dp[i+1]
                    break
                    
        # 返回整个字符串 s (即 s[0..len(s)-1]) 的拆分结果
        return dp[len(s)]