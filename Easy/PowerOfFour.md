# 问题分析：
给定一个整数 (32位有符整数型)，请写出一个函数来检验它是否是4的幂。
# 编程实现：
```C++
class Solution {
public:
    bool isPowerOfFour(int num) 
    {
        if(num<=0)
            return 0;
        if(num==0)
            return 1;
        while(num>1)
        {
            if(num%4!=0)
                return 0;
            else
                num=num/4;
        }
        return 1;
    }
};
```
# 总结体会：
当num是非正数的时候肯定不是4的幂，如果num为正数，若模4余数不为0，肯定不是4的幂，返回0，如果模4为0，则将n除以4，继续循环，最后如果循环结束，就说明num是4的幂，返回true即可。