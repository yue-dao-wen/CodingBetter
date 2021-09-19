// # include "datastruct.hpp"
# include "D:\\Efficiency\\50_Zhuanye\\10_Coding\\CodingBetter\\datastruct.hpp"
// tolearn:vscode怎么设置？
# include<vector>
using namespace std;


int PrintCommonValue(ListNode *head1, ListNode *head2){
    cout << "The common parts are: [";
    while(head1 != nullptr && head2 != nullptr){
        if(head1->val < head2->val){
            head1 = head1->next;
        }else if(head1->val > head2->val){
            head2 = head2->next;
        }else{
            cout << head1->val << ", ";
            head1 = head1->next;
            head2 = head2->next;
        }
    }
    cout << "]" << endl;
    return 0;
}


int DeleteLastKNode(ListNode *head, int k){
    // KIM: 不管任何时候都要检查输入是否合法！
    // todo: 公司代码里面的check_if是不是这个功能？干啥的？
    if(head == nullptr || k < 0){
        return -1;
    }
    ListNode *fast = head, *slow = head;

    while(k > 0){
    // for(int i=0; i<k; ++i){
        // cout << "fast->val=" << fast->val << endl;
        fast = fast->next;
        k --;
    }

    while(fast->next != nullptr){
        // cout << "fast->val=" << fast->val  << ", " << "slow->val=" << slow->val << endl;
        fast = fast->next;
        slow = slow->next;
    }
    slow->next = slow->next->next;

    return 0;
}


int run_delete_lastk_node(){
    vector<int> nums = {5, 4, 7, 2, 9};
    ListNode *head = BuildLinkList(nums);
    int k = 2;

    PrintLinkList(head);
    DeleteLastKNode(head, k);
    PrintLinkList(head);    
    
    return 0;
}

int run_print_common_value(){
    vector<int> nums1 = {1, 2, 3, 4, 5, 6};
    vector<int> nums2 = {0, 2, 3, 4, 7};
    ListNode *head1 = BuildLinkList(nums1);
    ListNode *head2 = BuildLinkList(nums2);
    PrintCommonValue(head1, head2);
    return 0;
}


int main(){
    // run_print_common_value();
    run_delete_lastk_node();
    
    return 0;
    

}