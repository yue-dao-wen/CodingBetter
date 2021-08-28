# include <vector>
using namespace std;

class Solution {
public:
    int getMaximumGenerated(int n) {
        // 空间优化？
        if(n < 0) return -1;
        if(n == 0) return 0;
        if(n == 1) return 1;

        vector<int> nums(n+1);
        nums[0] = 0;
        nums[1] = 1;
        int base;
        int ans = 1;
        for(int i = 2; i <= n; i ++){
            if(i % 2 == 0){
                base = i / 2;
                nums[i] = nums[base];
            }
            else{
                base = (i - 1) / 2;
                nums[i] = nums[base] + nums[base + 1];
            }
            
            if(nums[i] > ans) ans = nums[i];
        }
        
        return ans;

    }
};