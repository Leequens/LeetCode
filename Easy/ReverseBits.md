# 问题分析：
颠倒给定的 32 位无符号整数的二进制位。
# 编程实现：
```C++
class Solution {
public:
    uint32_t reverseBits(uint32_t n) 
    {
        uint32_t res=0;
        int i;
        for (i=0;i<32;i++) 
        {
            if (n&1==1) 
            {
                res=(res<<1)+1;
            } 
            else{
                res=res<<1;
            }
            n=n>>1;
        }
        return res;
    }
};
```
# 总结体会：
把要翻转的数从右向左一位位的取出来，如果取出来的是1，就将结果左移一位并且加上1；如果取出来的是0，我们将结果res左移一位，然后将n右移一位即可。