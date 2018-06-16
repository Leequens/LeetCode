# 问题分析:

给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如
1 -> A, 2 -> B, 3 -> C, 26 -> Z, 27 -> AA, 28 -> AB
# 编程实现：
```C++
class Solution {
public:
    string convertToTitle(int n) {
        string res="";
        while(n){
            if(n%26==0) 
            {
                res=res+'Z';
                n=n-26;
            }
            else
            {
                res+=n%26 - 1 + 'A';
                n-=n%26;
            }
            n/=26;
        }
        reverse(res.begin(),res.end());
        return res;
    }
};
```
# 总结体会：
从低位往高位求，每进一位，则把原数缩小26倍，再对26取余，之后减去余数，再缩小26倍，以此类推，可以求出各个位置上的字母。最后再将整个字符串翻转一下。
