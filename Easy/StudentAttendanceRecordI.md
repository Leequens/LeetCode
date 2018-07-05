# 问题分析：
给定一个字符串来代表一个学生的出勤纪录，这个纪录仅包含以下三个字符：
1. 'A' : Absent，缺勤
2. 'L' : Late，迟到
3. 'P' : Present，到场    
如果一个学生的出勤纪录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。
你需要根据这个学生的出勤纪录判断他是否会被奖赏。
# 编程实现：
```C++
class Solution {
public:
    bool checkRecord(string s) 
    {
        int countA=0,countL=0;
        for(char c: s)
        {
            if(c=='A')
            {
                countA++;
                if(countA==2)
                return 0;
                countL=0;
            }      
            else if(c=='L'&&countL<2)
                countL++;
            else if(c=='L'&&countL==2)
                return 0;
            else
                countL=0;
        }
        return 1;
    }
};
```
# 总结体会：
这道题抛开应用场景之后的意思其实就是让判断这个字符串中，是否有两个及以上的A，是否有连续三个以及以上的L，如果是的话就返回false，否则返回true，设置两个变量分别统计A和L的个数，countA当大于2的时候，就返回0，对于L就稍微有点麻烦，当遇到L并且countL=2的时候，直接返回0，如果小于2，就自增1。最后需要注意的是需要L之外的字母，countL都要置0.