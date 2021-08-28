#include<vector>
#include<map>
#include<algorithm>
using namespace std;

class Solution {
public:
    int timeCost(int from_id, vector<int> visited, map<int, vector<int>> outEdgeDict,  map<pair<int, int>, int> costDict){
        
        vector<int> to_ids = outEdgeDict[from_id];
        int n_to_id = to_ids.size();
        // todo: 有环怎么办？
        vector<int> all_path_cost;
        for(int i; i < n_to_id; i++){
            int to_id = to_ids[i];
            if(visited.find(to_id) != visited.end()){ // 这里为什么不能find?
                // todo:已经访问过了；
                continue;
            }
            visited.emplace_back(to_id);
            all_path_cost.emplace_back(costDict[{from_id, to_id}] + timeCost(to_id, visited, outEdgeDict, costDict));
        }

        int cost = max_element(all_path_cost.begin(), all_path_cost.end());
        return cost;

    }
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        //图遍历算法,广度遍历算法。
        // 最大的没有路的时间。
        map<int, vector<int>> outEdgeDict;
        map<pair<int, int>, int> costDict;

        int nEdge = times.size();
        for (int edgeId = 0; edgeId < nEdge; edgeId++){
            // 把所有信息装起来
            vector<int> curEdge = times[edgeId];
            int from_id = curEdge[0];
            int to_id = curEdge[1];
            int cost = curEdge[2];

            if(outEdgeDict.find(from_id) == outEdgeDict.end()){
                // 没有这个边
                outEdgeDict[from_id] = {};
            }
            outEdgeDict[from_id].emplace_back(to_id);
            costDict[{from_id, to_id}] = cost;
            
        }// for

        vector<int> visited;
        int res = timeCost(k, visited, outEdgeDict, costDict);
        return res


        




    }
};