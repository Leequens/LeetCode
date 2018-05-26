# 问题分析：
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。
# 编程实现：
```c++
class Solution {
public:
    int countSegments(string s)
    {
        int i,res=0,n=s.size();
        for(i=0;i<n;i++)
        {
            if(s[i]==' ') 
                continue;
            res++;
            while(i<n&&s[i]!=' ') 
                i++;
        }
        return res;
    }
};
```
# 总结体会：
遇到空格直接跳过，如果不是空格，则计数器加1，然后用个while循环找到下一个空格的位置，这样就遍历完了一个单词，再重复上面的操作直至结束，就能得到正确结果。