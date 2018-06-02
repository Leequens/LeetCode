# 问题分析：

在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

注意:
n 是正数且在32为整形范围内。
# 编程实现：
```C++
class Solution {
public:
    int findNthDigit(int n) 
    {
        long long len=1,cnt=9,start=1;
        while(n>len*cnt) 
        {
            n=n-len*cnt;
            len++;
            cnt=cnt*10;
            start=start*10;
        }
        start=start+(n-1)/len;
        string t=to_string(start);
        return t[(n-1)%len]-'0';
    }
};
```
# 总结体会：
数字中前九个数都是1位的，然后10到99总共90个数字都是两位的，100到999这900个数都是三位的，先定义个变量cnt，初始化为9，然后每次循环扩大10倍，再用一个变量len记录当前循环区间数字的位数，还需要一个变量start用来记录当前循环区间的第一个数字，n每次循环都减去len*cnt (区间总位数)，那么(n-1)/len就是目标数字在该区间里的坐标，加上start就是得到了目标数字。