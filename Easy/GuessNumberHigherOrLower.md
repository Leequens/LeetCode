# 问题分析：
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
每次你猜错了，我会告诉你这个数字是大了还是小了。
你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

-1 : 我的数字比较小
 1 : 我的数字比较大
 0 : 恭喜！你猜对了！
# 编程实现：
```C++
// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        if (guess(n)==0) return n;
        int a=1,b=n,	mid,t;
        while(a<b)
        {
            mid=a+(b-a)/2,t=guess(mid);
            if (t==0) return mid;
            else if(t==1) a=mid;
            else b=mid;
        }
        return a;
    }
};
```
# 总结体会： 
根据其给出的高了还是低了，然后使用二分法折半查找其答案即可。