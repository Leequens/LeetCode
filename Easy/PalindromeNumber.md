# 问题分析：
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 编程实现：
```C++
class Solution {
public:
    bool isPalindrome(int x)
    {
        int a=0,b=x;
        if(b<0)
            return false;
        while(b>0)
        {
            a=a*10+b%10;
            b=b/10;
        }
        return x==a;
    }
};
```

# 总结体会：
先将给出的整数进行反转，然后与原来的数作对比，如果不相等，则返回0，若相等，则返回1。 
