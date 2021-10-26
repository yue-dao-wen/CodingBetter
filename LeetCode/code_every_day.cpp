
# include<vector>
# include<functional>
// # include<math.h>
# include<algorithm>
# include<iostream>
# include<unordered_map>
# include<stack>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};


struct TrieNode{
    vector<TrieNode *> children;
    bool isEnd;
    TrieNode(){ // 为啥结构也尅有函数？初始化函数?
        this->children = vector<TrieNode *>(26, nullptr);
        this->isEnd = false;
    } 
};

void TrieNodeInsert(TrieNode *root, const string &word){
    // tolearn:为啥要用静态的？为啥要在函数里使用引用？
    TrieNode *node = root;
    for(auto c: word){
        if (node->children[c - 'a'] == nullptr){
            node->children[c - 'a'] = new TrieNode();
        }
        node = node->children[c - 'a'];
    }
    node->isEnd = true;
}


class Solution {
public:
    Node* flatten(Node* head) {
        function<Node*(Node*)> dfs = [&](Node* node){
            Node* cur = node;
            Node* last = nullptr;

            while(cur){
                Node* next = cur->next;

                if(cur->child){
                    Node* child_last = dfs(cur->child);

                    cur->next = cur->child;
                    cur->child->prev = cur;
                    cur->child = nullptr;

                    if(next){
                        child_last->next = next;
                        next->prev = child_last;
                    }

                    last = child_last;
                }
                else{
                    last = cur;
                }
                cur = next;
            }
            return last;
        };

        dfs(head);
        return head;
    } // func flatten

    int minMoves(vector<int>& nums) {
        int mmin = *min_element(nums.begin(), nums.end());
        int ans = 0;
        for(int n: nums){
            ans += (n - mmin);
        }
        return ans;
    } //func minMoves

    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        int n_kind = price.size();

        // todo:没做完的题
        // 只保留有用的礼包
        vector<vector<int>> special_valid;
        for (int sp_idx = 0; sp_idx < n_kind; sp_idx ++){
            int total_count = 0, totoal_price = 0;
            for (int i = 0; i < n_kind; i ++){
                total_count += special[sp_idx][i];
                totoal_price += special[sp_idx][i] * price[i];
            }

            if (total_count > 0 && totoal_price > special[sp_idx][n_kind]){
                special_valid.push_back(special[sp_idx]);
            }
        }

        int res = shoppingOffers_dfs(&needs, &price, special);
        return res;

    }//shoppingOffers

    int shoppingOffers_dfs(vector<int> *p_cur_needs, vector<int> *p_price, vector<vector<int>> &special){
        int min_price = 0;
        int n_kind = p_cur_needs->size();
        for (int idx = 0; idx < n_kind; idx ++){
            min_price += p_cur_needs->at(idx) * p_price->at(idx);
        }

        // 拿第每一个的时候都有可能拿任意一个礼包
        vector<int> next_needs;
        for (auto sp : special){
            // sp里每一个物品的数量都得<=cur_needs里面的数量
            for(int idx = 0; idx < n_kind; idx ++){
                if (sp[idx] <= p_cur_needs->at(idx)){
                    next_needs.push_back(p_cur_needs->at(idx) - sp[idx]);
                }else{
                    break;
                }
            }

            if (next_needs.size() == n_kind){
                int price = shoppingOffers_dfs(&next_needs, p_price, special);
                min_price = min(min_price, price + sp.end());
            }

        }
        return min_price;

    }// func shoppingOffers_dfs

    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n_row = matrix.size();
        if (n_row <= 0){
            return false;
        }
        int n_col = matrix[0].size();
        int x = 0, y = n_col - 1;
        while (x < n_row && y >= 0){
            if (matrix[x][y] > target){
                y -= 1;
            }else if (matrix[x][y] < target)
            {
                x += 1;
            }else{
                return true;
            }
        }
        return false;
        
    }// func searchMatrix
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int,int> next_bigger_map;
        stack<int> bigger_stack;
    
        int l2 = nums2.size();
        for (int i = l2 - 1; i >= 0; i --){
            while(!bigger_stack.empty() && bigger_stack.top() < nums2[i]){
                bigger_stack.pop();
            }
            next_bigger_map[nums2[i]] = bigger_stack.empty() ? -1: bigger_stack.top();
            bigger_stack.push(nums2[i]);
        }

        int l1 = nums1.size();
        vector<int> ret(l1) ;
        for(int i = 0; i < l1; i ++){
            ret[i] = next_bigger_map[nums1[i]];
        }

        return ret;
        

    }// func nextGreaterElement
};// class solution


int run_lc453(){
    vector<int> nums = {1, 2, 3};
    Solution sl;
    int ans = sl.minMoves(nums);
    std::cout << ans << std::endl;
    return 0;
}


int main(){
    run_lc453();
    return 0;
}