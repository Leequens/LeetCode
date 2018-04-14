# 问题分析：
给定一个罗马数字，将其转换成整数。
返回的结果要求在 1 到 3999 的范围内。

# 编程实现：
```C++
class Solution {
public:
    int romanToInt(string s)
    {
        int i,n,result;
        map<char,int>m;  
        m['I'] = 1;  
        m['V'] = 5;  
        m['X'] = 10;  
        m['L'] = 50;  
        m['C'] = 100;  
        m['D'] = 500;  
        m['M'] = 1000;  
        n=s.length();  
        result=m[s[n-1]];  
        for(i=n-2;i>=0;i--)
        {  
            if(m[s[i+1]]<=m[s[i]])  
                result=result+m[s[i]];  
            else 
                result=result-m[s[i]];  
        }  
        return result;  
    }         
};
```
# 总结体会：
因为不知道输入的字符串的长度，所以用map容器比较简单。map能自动建立Key－Value的对应，设定好每个罗马字母对应的阿拉伯数字后，用for循环从右到左开始
判断大下来选择相加还是相减，如果从左到右判断会稍微麻烦一些。
