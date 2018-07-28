# 问题分析：
给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。
# 编程实现：
```C++
class Solution {
public:
    bool hasAlternatingBits(int n)
    {
        int temp,res;
        temp=n%2;
        n=n/2;
        if(n==0)
            return 1;
        while(n)
        {
            res=n%2;
            n=n/2;
            if(temp==res)
                return 0;
            else
                temp=res;
        }
        return 1;
    }
};
```
#  总计体会：
这道题只要知道十进制转二进制的方法就不难，每次除以二的时候设置一个临时值，如果下一次除二得到的余数与上一次得到的相等，那么就返回false，如果循环能够正常结束，那么说明这个数是交替位二进制数，返回true。