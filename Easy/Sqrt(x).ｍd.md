# 问题分析：

实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去

# 编程实现：
```C++
class Solution {
public:
    int mySqrt(int x) 
    {
        int a=0,b=x,m;
        if(x<=1) return x;
        while(a<b)
        {
            m=(b+a)/2;
            if(x/m>=m) a=m+1;
            else b=m;
        }
        return b-1;
    }
};
```

# 总结体会：

最开始想到的是从0到x进行遍历，每一个值的平方与x比较，但是提交OJ的时候会超出时间限制。所以可以采用二分法来节省时间。