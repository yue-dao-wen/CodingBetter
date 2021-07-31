#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:

    int findRepeatNumber(vector<int>& nums) {
        int length = nums.size();
        int i = 0;
        while (i < length)
        {
            if(nums[i] == i)
            {
                i ++;
                continue;
            }
                
            if( nums[nums[i]] == nums[i]) // 还没还到对应位置上呢，发现对应位置上已经有正确的数字了
                return nums[i];
            swap(nums[i], nums[nums[i]]);
        }
        return 0;
    }

};




int main()
{
    vector<int> nums = {2, 3, 1, 0, 2, 5, 3};
    Solution *sl = new Solution();  // 为什么非要加上星号，作为地址才能用new呢？
    int res = sl->findRepeatNumber(nums);
    std::cout << res << std::endl; 

}