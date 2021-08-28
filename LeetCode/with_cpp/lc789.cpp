# include <stdlib.h>
# include <vector>
using namespace std;

class Solution {
public:
    bool escapeGhosts(vector<vector<int>>& ghosts, vector<int>& target) {
        // 不是同一个方向，阻碍者也会动。也是有意识的东。
        // 所有鬼的距离都要比我小。
        // 
        int my_distance = abs(target[0]) + abs(target[1]);
        int g_distance = 0;
        for(auto g : ghosts){
            g_distance = abs(g[0] - target[0]) + abs(g[1] - target[1]);
            if(g_distance <= my_distance) return false;
        }
        return true;
    }
};