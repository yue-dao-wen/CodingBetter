// # include "LeetCode\with_cpp\datastruct.hpp"
# include "datastruct.hpp"
# include <vector>
# include <iostream>

using namespace std;


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *pre=nullptr;
        while(head != nullptr){
            ListNode *tmp = head->next;
            head->next = pre;
            pre = head;
            head = tmp;
        }
        return pre;
    }
};



int main(){
    vector<int> nums = {1, 2, 3, 4, 5, 6};
    ListNode *head = BuildListNode(nums);
    Solution sl;
    ListNode *new_head = sl.reverseList(head);
    PrintListNode(new_head);
    
    return 0;

}