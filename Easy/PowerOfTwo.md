# 问题分析：
给定一个整数，写一个函数来判断它是否是 2 的幂次方。
# 编程实现：

```C++
class Solution {
public:
    bool isPowerOfTwo(int n) 
    {
        if(n<=0)
            return 0;
        else if(n<=2)
            return 1;
        while(n>2)
        {
            if(n%2==1)
                return 0;
            else
                n=n/2;
        }
        if(n==2)
            return 1;
    }
};
````
# 总结体会：
0，负数和奇数肯定不是2的幂，当n大于2的时候，就判断是不是奇数，如果是就判断为false，是偶数就除以2，然后继续判断。如果能够完成循环，就说明是2的幂，返回true即可。