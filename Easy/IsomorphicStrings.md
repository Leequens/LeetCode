# 问题分析：
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
# 编程实现：
```C++
class Solution {
public:
    bool isIsomorphic(string s, string t)
    {
        int i,m1[256]={0},m2[256]={0},n=s.size();
        for(i=0;i<n;i++)
        {
            if(m1[s[i]]!=m2[t[i]]) 
                return false;
            m1[s[i]]=i+1;
            m2[t[i]]=i+1;
        }
        return true;
    }
};
```
# 总结体会：
用一个256大小的数组来代替哈希表，并初始化为0，然后遍历原字符串，分别从源字符串和目标字符串取出一个字符，然后分别在两个哈希表中查找其值，若不相等，则返回false，若相等，将其值更新为i+1。