# 问题分析：
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

注意:

1. 给定的整数保证在32位带符号整数的范围内。
2. 你可以假定二进制数不包含前导零位。
# 编程实现：
```C++
class Solution {
public:
    int findComplement(int num) 
    {
        int i;
        bool start=false;
        for (i=31;i>=0;i--)
        {
            if(num&(1<<i)) 
                start=true;
            if(start)
                num=num^(1<<i);
        }
        return num;
    }
};
```
# 总结体会： 
应该从高往低遍历，因为起始位置上从最高位的1开始的，前面的0是不能被翻转的，遍历时如果遇到第一个1了后，我们的flag就赋值为true，然后就可以进行翻转了，翻转的方法就是对应位异或一个1即可。