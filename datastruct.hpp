# include<iostream>
# include<vector>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}  // todo:这是啥？和类的构造函数的区别是啥？
};

int PrintListNode(ListNode *head){
    cout << "The ListNode = [";
    while(head != nullptr){
        cout << head->val << ", ";
        head = head->next;
    }
    cout << "]" << endl;
    return 0;
}

ListNode* BuildListNode(vector<int> nums){
    int n = nums.size();
    if(n == 0){
        return nullptr;
    }
    ListNode *p_dump = new ListNode(0), *cur = new ListNode(nums[0]);
    // ListNode *p_dump, *cur; 这种是错的
    p_dump->next = cur;
    for(int i=1; i < n; ++i){
        ListNode *node = new ListNode(nums[i]);
        // ListNode *node;  这种是错的
        node->val = nums[i];
        // cout << nums[i] << endl;
        cur->next = node;
        cur = cur->next;
    }
    PrintListNode(p_dump->next);
    return p_dump->next;
}
