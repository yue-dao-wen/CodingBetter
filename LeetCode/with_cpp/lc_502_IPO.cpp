# include<vector>
# include<math.h>
# include<algorithm>
# include<queue>

using namespace std;

typedef pair<int, int> pairr;

class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        
        priority_queue<int, vector<int>, less<int>> q_able;
        vector<pairr> cp_pairs;

        int n = capital.size();
        for(int i = 0; i < n; ++i){
            cp_pairs.push_back({capital[i], profits[i]});
        }
        sort(cp_pairs.begin(), cp_pairs.end()); // todo: 不需要指定key吗？
        
        int idx = 0;
        for(int i = 0; i < k ; ++i){
            while(idx < n && cp_pairs[idx].first <= w){
                q_able.push(cp_pairs[idx].second);
                idx ++;
            }
            if(!q_able.empty){
                w += q_able.top(); // top和pop分开
                q_able.pop();
            }
            else{
                break;
            }
        
        
        }
        return w;
    }
};