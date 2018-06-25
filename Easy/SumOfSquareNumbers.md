# 问题分析：

给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a<sup>2</sup> + b<sup>2</sup> = c。
# 编程实现：
```C++
class Solution {
public:
    bool judgeSquareSum(int c)
    {
        int a,b;
        for(int i=0;i<=sqrt(c);i++)
        {
            if(i*i==c)
                return 1;
            a=c-i*i;
            b=sqrt(a);
            if(b*b==a)
                return 1;
        }
        return 0;
    }
};
```
# 总结体会：
从0判断到c的平方根就可以，因为超过平方根肯定平方大于c，先判断i的平方是否等于c，如果等于就返回1，不等的话就判断c于i方的差，如果差值也是平方数，那么这个c肯定是两数的平方和。