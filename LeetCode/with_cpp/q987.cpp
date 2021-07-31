// Definition for a binary tree node.
struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };

#include<vector>
#include<map>
using namespace std;

class Solution {
public:
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        // 每个矩阵的元素也是矩阵。
        // 怎么用字典和矩阵？
        
        map<int, map<int, int>> ColDict;
        map<int, int> RowDict;  // c++ 变量命名的方式是啥？
        // c++ 里怎么生成有顺序的dict？

        // 遍历一遍树，确定每个结点的rowid 和colid，并放在dict里。
        



    }
};