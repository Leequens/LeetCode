# 问题分析:
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
# 编程实现：
```C++
class Solution {
public:
    int strStr(string haystack, string needle)
    {
        int i,j,a,b;
        a=haystack.size();
        b=needle.size();
        if (needle.empty()) 
            return 0;      
        if (a<b) 
            return -1;
        for (i=0;i<=a-b;i++) 
        {
            for(j=0;j<b;j++) 
            {
                if(haystack[i+j]!=needle[j]) 
                    break;
            }
            if(j==b) 
                return i;
        }
        return -1;
    }
};
```
# 总结体会：
首先判断needle为0时，返回0，needle的长度大于haystack的时候，返回-1。
对于needle每一个字符都要遍历一遍字符串，相比较不同时跳出循环。如果最后j与needle长度相同，则说明长字符串中含有短的，则返回初始坐标。
