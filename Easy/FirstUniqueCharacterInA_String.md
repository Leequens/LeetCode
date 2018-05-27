# 问题分析：
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 编程实现：
```C++
class Solution {
public:
    int firstUniqChar(string s)
    {
        int i;
        unordered_map<char,int>m;
        for(i=0;i<s.size();i++) 
            m[s[i]]++;
        for (i=0;i<s.size();i++)
        {
            if(m[s[i]]==1) 
                return i;
        }
        return -1;
    }
};
```
# 总结体会：
用哈希表建立每个字符和其出现次数的映射，然后按顺序遍历字符串，找到第一个出现次数为1的字符，返回其位置，如果跳出循环，则说明每个字母都重复了，返回-1。