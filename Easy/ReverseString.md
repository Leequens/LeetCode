# 问题分析:
请编写一个函数，其功能是将输入的字符串反转过来。
# 编程实现:
```C++
class Solution {
public:
    string reverseString(string s)
    {
        int left=0,right=s.size()-1;
        char t;
        while(left<right) 
        {
            t=s[left];
            s[left]=s[right];
            left++;
            s[right]=t;
            right--;
        }
        return s;
    }
};
```
# 总结体会：
设置一个中间变量，然后字符串的两边往中间遍历字符串，交换两边的字符即可。