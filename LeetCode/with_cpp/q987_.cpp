#include<vector>
#include<functional>
#include<algorithm>

#include "datastruct.hpp"

using namespace std;

class Solution{
public:
    vector<vector<int>> verticalTraversal(TreeNode* root){
        vector<tuple<int, int, int>> nodes;

        function<void(TreeNode*, int, int)> dfs = [&](TreeNode* node, int row, int col){
            if(!node){
                return;
            }
            nodes.emplace_back(col, row, node->val);
            dfs(node->left, row+1, col-1);
            dfs(node->right, row+1, col-1);
        }; // 直接定义一个函数不行吗？为什么要用function<>这个模板？（是模板吧？

        dfs(root, 0, 0);
        sort(nodes.begin(), nodes.end());   // 先按照begin()位置的元素排序，然后再按照end()位置的排序？
        vector<vector<int>> ans;
        int lastcol = INT_MIN;
        for (const auto&[col, row, value]:nodes){ // 这是什么用法？ # https://bbs.csdn.net/topics/392167864?page=1
            if(col != lastcol){
                lastcol = col;
                ans.emplace_back(); // 这啥都没有放？
            }
            ans.back().push_back(value);
        }
        return ans;

    }

};
