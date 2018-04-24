# 问题分析：
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

# 编程实现：
```C++
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i=m+n;
        while(m>0&&n>0)
        {
            if(nums1[m-1]>nums2[n-1])
            {
                nums1[i-1]=nums1[m-1];
                m--;
            } 
            else 
            {
                nums1[i-1]=nums2[n-1];
                n--;
            }
            i--;
        }
        while(n>0)
        {
            nums1[i-1]=nums2[n-1];
            n--;
            i--;
        }
    }
};
```
# 总结体会：
如果从前往后按从小到大排序，会比较麻烦，所以从数组最后一位开始比较，谁大谁就排在最后，如果m>n，排完nums2之后mnums1剩下的正好就可以构成新数组，如果m<n，再把nums2剩下的中元素写入nums1即可。