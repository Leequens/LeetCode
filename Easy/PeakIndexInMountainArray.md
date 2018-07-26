# 问题分析：
我们把符合下列属性的数组 A 称作山脉：
*  A.length >= 3 
*  存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。
# 编程实现：
```C++
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A)
    {
        for(int i=0;i<A.size()-1;i++)
            if(A[i]>A[i+1])
                return i;   
    }
};
```
# 总结体会:
直接判断返回数组中最大元素的索引即可。
