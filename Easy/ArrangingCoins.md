# 问题分析：
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内。

# 编程实现：
```C++
class Solution {
public:
    int arrangeCoins(int n) 
    {
        if(n==0) return 0;
        int i=1,res=n-1;
        while(res>=i+1)
        {
            i++;
            res=res-i;
        }
        return i;
    }
};
```

# 总结体会：
从第一行开始，一行一行的从n中减去，如果此时剩余的硬币没法满足下一行需要的硬币数了，直接返回当前行数即可。