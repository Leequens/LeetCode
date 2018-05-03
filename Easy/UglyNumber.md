# 问题分析：

编写程序判断给定的数是否为丑数。

丑数就是只包含质因子 2, 3, 5 的正整数。例如， 6, 8 是丑数，而 14 不是，因为它包含了另外一个质因子 7。

注意：

1、 1也可以被当做丑数。
2、 输入不会超过32位整数的范围。
# 编程实现：
```c++
class Solution {
public:
    bool isUgly(int num) 
    {
        while(num>=2)
        {
            if(num%2==0)
                num=num/2;
            else if (num%3==0)
                num=num/3;
            else if (num%5==0)
                num=num/5; 
            else return 0;
        }
        if(num==1)
            return 1;
        else return 0;
    }
};
```
# 总结体会：
丑数就是指其质数因子只能是2,3,5。最直接的办法就是不停的除以这些质数，如果剩余的数字是1的话就是丑陋数了。