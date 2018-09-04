# 问题分析：
给定两个整数 L 和 R ，找到闭区间 [L, R] 范围内，计算置位位数为质数的整数个数。

（注意，计算置位代表二进制表示中1的个数。例如 21 的二进制表示 10101 有 3 个计算置位。还有，1 不是质数。）

# 编程实现：
```C++
class Solution {
public:
    int countPrimeSetBits(int L, int R) {
        int res = 0;
        for (int i = L; i <= R; ++i) {
            int t = i, cnt = 0;
            while (t > 0) {
                if (t & 1 == 1) ++cnt;
                t >>= 1;
            }
            bool succ = true;
            for (int j = sqrt(cnt); j > 1; --j) {
                if (cnt % j == 0) {
                    succ = false; break;
                }
            }
            if (succ && cnt != 1) ++res;
        }
        return res;
    }
};
```
# 总结体会：
遍历整数范围[L, R]中的每一个数字，然后先统计出所有非零位个数cnt，通过和1相与，再右移一位的方式。然后就是来判断这个cnt是否是质数，结果加1即可。