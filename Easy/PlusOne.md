# 问题分析：
给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

# 编程实现：
```C++
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int i;   
        for(i=digits.size()-1;i>=0;i--)
        {
            if(digits[i]==9)
                digits[i]=0;
            else 
            {
                digits[i]++;
                return digits;
            }
        }
        if(digits[0]==0)
            digits.insert(digits.begin(),1);
        return digits;
    }
};
```
# 总结体会：
遍历数组判断最后一个数字是否为9，如果不是9，就加1，然后返回，如果是9，就赋值为0，继续看前一位的数值。
最后检查是不水第一位也变成了0，如果是的话，在其前面插入1并返回。