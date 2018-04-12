# 问题分析：
给定一个范围为 32 位 int 的整数，将其颠倒。
注意:
假设我们的环境只能处理 32 位 int 范围内的整数。根据这个假设，如果颠倒后的结果超过这个范围，则返回 0。

# 编程实现：
```C++
class Solution {
public:
    int reverse(int x)
    {
        long long a=0;
        int int_max=2147483647,int_min=-2147483648;
        while(x!=0)
        {
            a=a*10+x%10;
            x=x/10;
        }
        if(a<int_min||a>int_max)
        {
            a=0;
        }
        return a;
    }
};
```
# 总结体会：
将x取个位数的办法就是将x对10取余，取出后放在a的最高位。题中第二个条件规定反转后的数不能溢出int范围，即a有可能会溢出int范围，所以最开始要对a定义成long型变量，最后再加一个条件语句判断a是否溢出即可。
