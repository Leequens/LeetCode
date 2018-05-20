# 问题分析：
给出一个整数，写一个函数来确定这个数是不是3的一个幂。
# 编程实现：
```C++
class Solution {
public:
    bool isPowerOfThree(int n) 
    {
        if(n<=0)
            return 0;
        if(n==0)
            return 1;
        while(n>1)
        {
            if(n%3!=0)
                return 0;
            else
                n=n/3;
        }
        return 1;
    }
};
```
# 总结体会：
当n位非正数的时候肯定不是3的幂，如果n为正数，若模3余数不为0，肯定不是3的幂，如果模3位0，则将n除以三，继续循环，最后如果循环结束，肯定3的幂，返回true即可。