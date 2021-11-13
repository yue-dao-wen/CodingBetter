
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

class TrieNode{
public:
    // TrieNode()的括号里放什么？
    TrieNode(): children(26, nullptr), is_end(false), val(0), sum(0) {} // 为什么要在这里初始化?
    
    void insert(std::string word, int val, int delta);
    TrieNode* get_last_node(std::string word);

    // 什么时候private呢？
    bool is_end;
    int val;
    int sum;
    vector<TrieNode *> children;  // vector<TrieNode *> children;(26, nullptr)为什么会提示 “应输入类型说明符”
    

};

void TrieNode::insert(std::string word, int val, int delta){
    TrieNode *node = this;
    int c_idx;
    for(auto c: word){
        c_idx = c - 'a';
        if(node->children[c_idx] == nullptr){
            node->children[c_idx] = new TrieNode();
        }
        node = node->children[c_idx];
        node->sum += delta;
    }
    node->is_end = true;
    node->val = val;

}

TrieNode* TrieNode::get_last_node(std::string prefix){
    TrieNode *node = this;
    for (auto c: prefix){
        if (node->children[c - 'a'] == nullptr){
            return nullptr;
        }else{
            node = node->children[c - 'a'];
        }
    }
    return node;
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
                // min_price = min(min_price, price + sp.end());
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

class MapSum_Map {
public:
    MapSum_Map() {}

    void insert(string word, int wval) {
        int delta = wval;
        if(word_map.count(word)){  // 判断存在
            delta -= word_map[word]; // 计算新值和旧值的变量
        }
        word_map[word] = wval;
        for(int i = 0; i < word.size(); i++){
            prefix_map[word.substr(0, i+1)] += delta;
        }
    }
    
    int sum(string prefix) {
        return prefix_map[prefix]; // 默认初始化就为0了。
    }
private:
    // 什么情况下需要private？
    unordered_map<std::string, int> word_map; 
    unordered_map<std::string, int> prefix_map;
};

class MapSum {
public:
    MapSum() {}

    void insert(std::string word, int wval);
    int sum(std::string prefix);

private:
    TrieNode* root = new TrieNode();    // 这里要写成new 的形式！不能下成TrieNode *root; 为啥呢?
    unordered_map<std::string, int> word_map;
};

 void MapSum::insert(string word, int wval){
        int delta = wval;
        if(word_map.count(word)){
            delta -= word_map[word];
        }
        word_map[word] = wval;
        root->insert(word, wval, delta);
    }

int MapSum::sum(std::string prefix){
    TrieNode* node = root->get_last_node(prefix);
    if(node == nullptr){
        return 0;
    }else{
        return node->sum;
    }
}

int run_lc677(){
    MapSum sl;
    sl.insert("leetcode", 2);
    sl.insert("luhan", 7);
    int cnt = sl.sum("l");
    cout << cnt << endl;
    return 0;
}


int run_lc453(){
    vector<int> nums = {1, 2, 3};
    Solution sl;
    int ans = sl.minMoves(nums);
    std::cout << ans << std::endl;
    return 0;
}


int main(){
    // run_lc453();
    run_lc677();
    return 0;
}