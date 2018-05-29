# 问题分析：
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
# 编程实现：
```C++
class Solution {
public:
    bool repeatedSubstringPattern(string str)
    {
        int n=str.size(),i,j,c;
        string t;
        for (i=n/2;i>=1;i--) 
        {
            if(n%i==0) 
            {  
                c=n/i;
                t="";
                for(j=0;j<c;j++) 
                {
                    t=t+str.substr(0, i); 
                }
                if(t==str)
                return true;
            }
        }
        return false;
    }
};
```
# 总结体会：
从原字符串长度的一半开始遍历，如果当前长度能被总长度整除，说明可以平分成子字符串，然后把这些子字符串拼接起来看跟原字符串是否相等。 如果拆完了都不相等，返回false。