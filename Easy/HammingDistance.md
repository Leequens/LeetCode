# 问题分析：
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。
# 编程实现：
```C++
class Solution {
public:
    int hammingDistance(int x, int y) 
    {
        int z=x^y,res=0;              
        while(z!=0){      
            if(z&1)
            {                   
                res++;
            }
            z=z>>1;                     
        }
        return res;
    }
};
```
# 总结体会：
汉明距离指的是两个二进制数对应位不同的位置的数目，所以可以采用异或来解决，用z来存放x与y异或的结果，res存放答案，如果z最后一位是1，res就自加，然后再把z右移一位，最终即可得到答案。