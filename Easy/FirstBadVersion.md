# 问题分析：
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
# 编程实现：
```C++
// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) 
    {
        int left=1,right=n;
        while (left<right)
        {
            int mid=left+(right-left)/2;
            if(isBadVersion(mid)) 
                right=mid;
            else 
                left=mid+1;
        }
        return left;
    }
};
```
# 总结体会：
用二分法来找这个边界，对mid值调用API函数，如果是坏版本，说明边界在左边，则把mid赋值给right，如果是好版本，则说明边界在右边，则把mid+1赋给left，最后返回left即可。