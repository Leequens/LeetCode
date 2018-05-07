# 问题分析：
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

注意：不要使用任何内置的库函数，如  sqrt。

# 编程实现：
```C++
class Solution {
public:
    bool isPerfectSquare(int num) 
    {
        long a=0,b=num,mid,c;
        if(num==1) return 1;
        while(a<=b)
        {
           mid=(a+b)/2;
           c=mid*mid;
           if(c==num) return 1;
           else if(c<num) a=mid+1;
            else b=mid-1;
        }
        return 0;
    }
};
```
# 总结体会：
和之前的球开方一样，不能从1到num遍历数组，效率会比较低，应该使用二分法查找，不会超出时间限制。