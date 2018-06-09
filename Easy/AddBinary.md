# 问题分析：
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。
# 编程实现：
```c++
class Solution {
public:
    string addBinary(string a, string b) {
        string res;
        int na=a.size(),nb=b.size(),n=max(na, nb);
        int i;
        bool carry=false;
        if(na>nb)
        {
            for(i=0;i<na-nb;i++) 
                b.insert(b.begin(), '0');
        }
        else if(na>nb)
        {
            for(i=0;i<nb-na;i++) 
                a.insert(a.begin(), '0');
        }
        for (i=n-1;i>=0;i--) 
        {
            int tmp=0;
            if(carry)
                tmp=(a[i]-'0')+(b[i] -'0')+1;
            else tmp=(a[i]-'0')+(b[i]-'0');
            if (tmp==0)
            {
                res.insert(res.begin(),'0');
                carry=false;
            }
            else if(tmp==1) 
            {
                res.insert(res.begin(), '1');
                carry=false;
            }
            else if (tmp==2) 
            {
                res.insert(res.begin(), '0');
                carry=true;
            }
            else if(tmp==3)
            {
                res.insert(res.begin(), '1');
                carry=true;
            }
        }
        if (carry)
            res.insert(res.begin(),'1');
        return res;
    }
};
```
# 总结体会：
新建一个string类型的变量，它的长度是两条输入string中的较大的那个，并且把较短的那个输入string通过在开头加字符‘0’来补的较大的那个长度。这时候我们逐个从两个string的末尾开始取出字符，然后转为数字，想加，如果大于等于2，则标记进位标志carry，并且给新string加入一个字符‘0’。