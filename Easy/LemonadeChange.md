# 问题分析：
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

# 编程实现：
```C++
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) 
    {
        int count5=0,count10=0;
        if(bills[0]!=5)
            return 0;
        for(int i=0;i<bills.size();i++)
        {
            if(bills[i]==5)
                count5++;
            else if(bills[i]==10)
            {
                if(count5==0)
                    return 0;
                count5--;
                count10++;
            }
            else 
            {
                if(count5>0&&count10>0)
                {
                    count5--;
                    count10--;
                }
                else if(count5>=3)
                    count5=count5-3;
                else
                    return 0;
            }
        }
        return 1;
    }
};
```
# 总结体会：
设置两个计数器，当收到五元钱时，count5++；当收到十元钱时，判断count5是否为0，如果为0直接返回false，如果不为0，count5++，coount10--；当收到二十元钱时，先看是否有一个五元和十元，如果没有再看是否有三个五元，如果还是没有就返回false。最后遍历完后如果没有返回值，说明可以找零，返回true。