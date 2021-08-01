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

class NodeDict
{
private:
    /* data */
    // ？？：要定义一个结构的时候，变量应该是
    
};




class Solution {
public:
    
    void BreadthFirstTraversal(TreeNode* root, map<int, map<int, int>>& ColDict,map<int, int>& RowDict){
        // 输入参数的类型也太长了吧？怎么短一点？结构？类？
    }
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        // 每个矩阵的元素也是矩阵。
        // 怎么用字典和矩阵？
        
        map<int, map<int, int>> ColDict;
        map<int, int> RowDict;  // c++ 变量命名的方式是啥？
        // c++ 里怎么生成有顺序的dict？

        // 遍历一遍树，确定每个结点的rowid 和colid，并放在dict里。




    }
};