# include<iostream>
# include<vector>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}  // todo:这是啥？和类的构造函数的区别是啥？
};


struct ListDoubleNode
{
    int val;
    ListDoubleNode *next;
    ListDoubleNode *last;
    ListDoubleNode(int x) : val(x), next(nullptr), last(nullptr) {}
};

int PrintLinkList(ListNode *head){
    cout << "The ListNode = [";
    while(head != nullptr){
        cout << head->val << ", ";
        head = head->next;
    }
    cout << "]" << endl;
    return 0;
}

int PrintDoubleLinkList(ListDoubleNode *head){
    // todo:有很多功能相同的函数，用模板可以解决不？还是用函数重载？
    // tolearn: c++的默认参数怎么设置？
    cout << "The DoubleLinkList = [";
    while(head->next != nullptr){
        cout << head->val << ", ";
        head = head->next;
    }
    cout <<  head->val << "], and in reverse, the DoubleLinkList = [";

    while(head->last != nullptr){
        cout << head->val << ", ";
        head = head->last;
    }
    cout << head->val << "]." << endl;
    return 0;
}

ListNode* BuildLinkList(vector<int> nums){
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
    // PrintLinkList(p_dump->next);
    return p_dump->next;
}

ListDoubleNode* BuildDoubleLinkList(vector<int> nums){
    // todo: 是不是可以做成一个函数的模板？
    int n = nums.size();
    if(n == 0){
        return nullptr;
    }
    ListDoubleNode *p_dump = new ListDoubleNode(-1), *cur = new ListDoubleNode(nums[0]);
    p_dump->next = cur;
    for(int i=1; i < n; ++i){
        ListDoubleNode *node = new ListDoubleNode(nums[i]);
        node->val = nums[i];
        cur->next = node;
        node->last = cur;
        cur = cur->next;
    }
    return p_dump->next;
}
