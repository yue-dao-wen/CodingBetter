#include <vector>
#include <stdio.h>
# include <iostream>
using namespace std;

class Solution {
public:
    int countRange(vector<int>& nums, int length, int start, int middle)
    {
        // std::cout << nums << std::endl;
        if(nums.size() == 0)
        {
            return 0;
        }
        // std::cout <<"The length is " << length <<  "." << std::endl;
        int count = 0;
        for (int i = 0; i < length; i++)
        {
            if(nums[i] >= start && nums[i] <= middle)
            {
                count ++;
            }
                
        }
        return count;
    }

    int findRepeatNumber(vector<int>& nums) {

        // int length = sizeof(nums) / sizeof(int);
        int length = nums.size();
        int start = 0;
        int end = length - 1;
        while (end >= start)
        {
            int middle = start + ((end - start) >> 1);
            int count = countRange(nums, length, start, middle);
            // std::cout <s"The count is " << count <<  "." << std::endl;
            if (end == start)
            {
                if(count > 1) return end;
                else break;
            }

            if (count > (middle - start + 1))
                end = middle;
            else
                start = middle + 1;
        }
        return -1;
    }
};

int main()
{
    vector<int> nums = {2, 3, 1, 0, 2, 5, 3};
    Solution *slution = new Solution();
    int n = slution->findRepeatNumber(nums);
    // printf("%d", n); // ?? 为啥不能用这个？用这个就出错？？
    // std::cout << "The result is " << n << "." << std::endl;
    std::cout  << n <<std::endl;
    return 0;
}