#include<queue>
#include<unordered_set>
using namespace std;

class Solution{
public:
    int nthSuperUglyNumber(int n, vector<int>& primers){
        unordered_set<long> seen;
        priority_queue<long, vector<long>, greater<long>> heap; // greater是什么？
        seen.insert(1);
        heap.push(1);
        int ugly = 0;
        for(int i=0;i<n;i++){
            long cur = heap.top();
            heap.pop();
            ugly = (int) cur; // 为什么要强制数据转换？
            for(int p:primers){
                long next = cur * p;
                if (seen.insert(next).second){ // cy??:这啥意思？
                    heap.push(next);
                }
            }
        }
        return ugly;
    }
};
