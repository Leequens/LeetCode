# 问题分析：
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
# 编程实现：
```C++
class Solution {
public:
    bool isAnagram(string s, string t)
    {
        int i;
        if(s.size()!=t.size()) 
            return false;
        int m[26]={0};
        for (i=0;i<s.size();i++) 
            m[s[i]-'a']++;
        for (i=0;i<t.size();i++) 
        {
            if(--m[t[i]-'a']<0) 
                return false;
        }
        return true;
    }
};  
```
# 总结体会：

先判断两个字符串长度是否相同，不相同直接返回false。然后把s中所有的字符出现个数统计起来，存入一个大小为26的数组中，因为题目中限定了输入字符串为小写字母组成。然后我们再来统计t字符串，如果发现不匹配则返回false。