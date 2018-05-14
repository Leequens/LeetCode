# 问题分析：
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
# 编程实现：
```C++
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int mx1 = INT_MIN, mx2 = INT_MIN, mx3 = INT_MIN;
        int mn1 = INT_MAX, mn2 = INT_MAX;
        for (int num : nums) {
            if (num > mx1) {
                mx3 = mx2; mx2 = mx1; mx1 = num;
            } else if (num > mx2) {
                mx3 = mx2; mx2 = num;
            } else if (num > mx3) {
                mx3 = num;
            }
            if (num < mn1) {
                mn2 = mn1; mn1 = num;
            } else if (num < mn2) {
                mn2 = num;
            }
        }
        return max(mx1 * mx2 * mx3, mx1 * mn1 * mn2);
    }
};
```
# 总结体会：
原本对数组排序后将最大的三个数相乘，结果不能通过OJ，忽略了负数的部分，有负数的时候只要把最小的两个负数和最大的一个正数相乘，返回即可。