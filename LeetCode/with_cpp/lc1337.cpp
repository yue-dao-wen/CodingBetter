#include<vector>
#include <algorithm>
using namespace std;


class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        // 总是排在比较靠前的位置，可以有简单的方法
        int nRow = mat.size();
        int nCol = mat[0].size();
        vector<int> ans = {};
        
        for (int j = 0; j < nCol; j++){
            for (int i = 0; i < nRow; i++){
                if (mat[i][j] == 0 && std::find(ans.begin(), ans.end(), i) == ans.end()){
                    ans.emplace_back(i);
                    if(ans.size() == k){
                        break;
                    }
                }
            }//for

            if(ans.size() == k){
                break;
            }//if
        }//for

        int i = 0;
        while (ans.size() < k && i < nRow)
        {
            if(std::find(ans.begin(), ans.end(), i) == ans.end()){  
                // 如果没找到，加进来
                ans.emplace_back(i);
            }
            i ++;
        }

        return ans;
    }
};//Solution

int main(){
    
    vector<vector<int>> mat;
    
    vector<int> B1 = {1,1,0,0,0};
    vector<vector<int>> mat = vector<vector<int>>(5, vector<int>(5)) = {{1,1,0,0,0}, {1,1,1,1,0},{1,0,0,0,0},{1,1,0,0,0},{1,1,1,1,1}};
    return 0;
}