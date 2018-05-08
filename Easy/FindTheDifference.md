# 问题分析：
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。
# 编程实现：
```C++
class Solution {
public:
    char findTheDifference(string s, string t)
    {
        char res=0;
        int i;
        for(i=0;i<s.size();i++)
        {
            res=res-s[i];
        }
        for(i=0;i<t.size();i++)
        {
            res=res+t[i];
        }
        return res;
    }
};
```
# 总结体会：
用0减去原字符串里的所有元素，再加上新字符串的所有元素，相同的字符一减一加也就抵消了，剩下的就是后加的那个字符。