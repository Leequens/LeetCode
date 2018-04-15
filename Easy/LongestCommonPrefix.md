# 问题分析：
编写一个函数来查找字符串数组中的最长公共前缀。

# 编程实现：
```C++
class Solution{
public:
    string longestCommonPrefix(vector<string>& strs) 
    {
        string a = "";
        int i,j;
        char b;
        if(strs.empty()) return a;
        for(j= 0; j<strs[0].size(); j++)
        {
            b=strs[0][j];
            for (i=1;i<strs.size();++i) 
            {
                if(j>=strs[i].size()||strs[i][j]!= b) 
                {
                    return a;
                }
            }
            a.push_back(b);
        }
        return a;
    }
};
```
# 总结体会：
最长公共前缀肯定不会比整个数组中最短的长，顶多相等。具体思路是每次取第一个字符串的某一个位置的字符，然后遍历其他字符串相同位置的字符看是否相同，
相同则存入结果，不同则返回答案。
