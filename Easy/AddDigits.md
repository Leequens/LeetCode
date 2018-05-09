# 问题分析：
给一个非负整数 num，反复添加所有的数字，直到结果只有一个数字。

例如:

设定 num = 38，过程就像： 3 + 8 = 11, 1 + 1 = 2。 由于 2 只有1个数字，所以返回它。

# 编程实现：
```C++
class Solution {
public:
    int addDigits(int num)
    {
        int res;
        if(num<10)
            return num;
        while(num/10>0)
        {
            res=0;
            while(num>0)
            {
                res=res+num % 10;
                num=num/10;
            }
            num=res;
        }
        return res;
    }
};
```
# 总结体会：
当num小于10的时候直接返回num即可，num大于10的时候把各个位上的数字相加，若结果还大于10的话，则继续相加，直到数字小于10为止。