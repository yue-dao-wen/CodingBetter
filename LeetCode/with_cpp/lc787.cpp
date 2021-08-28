# include<vector>
# include<math.h>
using namespace std;


class Solution {
private:
    // 为啥是private?
    // 这些符号是啥意思？
    // 为啥是这个数字？
    static constexpr int INF = 10000*101 + 1;
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // 有大小的二维数组怎么整？
        vector<vector<int>> cost(k+2, vector<int>(n, INF));
        cost[0][src] = 0;
        for(int t = 1; t< k+2; t++){
            for(auto&& f: flights){ // 为啥要加&&？
                int j = f[0], i=f[1], p=f[2];
                cost[t][i] = min(cost[t][i], cost[t-1][j] + p);
            }
        }

        int ans = INF;
        for(int t=1;t<k+2;++t){
            ans = min(ans, cost[t][dst]);
        }

        return(ans == INF? -1: ans);    // 这种一定要括号括起来吗
        

    }
};