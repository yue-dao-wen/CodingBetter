# include <vector>
# include <limits.h>
# include <algorithm>
# include <iostream>
using namespace std;

class Solution {
public:
    int minSteps(int n) {
        vector<int> dp(n+1);
        int j = 1;
        for(int i=2; i <= n; ++i){
            dp[i] = INT_MAX;
            for(int j = 1; j * j <= i; ++j){
                if(i % j == 0){
                    dp[i] = min(dp[i], dp[j] + i / j);
                    dp[i] = min(dp[i], dp[i / j] + j);
                }
            }//for
        }//for
        return dp[n];
    }
};

int main(){
    int n = 9;
    Solution sl;
    int res = sl.minSteps(n);
    cout << "the res = " << res << endl;
    
}