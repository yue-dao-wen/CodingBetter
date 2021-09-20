# include "datastruct.hpp"
# include<vector>
# include<math.h>
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

int RemoveLastKthNode(ListNode *head, int k){
    // KIM: 不管任何时候都要检查输入是否合法！
    // todo: 公司代码里面的check_if是不是这个功能？干啥的？
    if(head == nullptr || k < 1){
        return -1;
    }
    int n = 0;
    ListNode *cur = head;
    while(cur != nullptr){
        cur = cur->next;
        n ++;
    }
    
    if(k > n){
        cout << " k= " << k << "> length_of_link_list = n" << ", new k = " << k % n << endl;
        k = k % n; //取余数？
    }

    ListNode *fast = head, *slow = head;

    while(k > 0){
    // for(int i=0; i<k; ++i){
        // cout << "fast->val=" << fast->val << endl;
        // KIM：如果K的值大于链表的长度？？这个会出错。
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


int RemoveLastKthDoubleNode(ListDoubleNode *head, int k){
    if(head == nullptr) return -1;
    
    while(head->next != nullptr){
        head = head->next;
    }

    while(k != 0){
        head = head->last;
        k --;
    }

    head->next = head->next->next;
    head->next->last = head;

    return 0;
}

ListNode* RemoveMidListNode(ListNode *head){
    if(head == nullptr || head->next == nullptr){
        return nullptr;
    }
    
    if(head->next->next == nullptr){
        return head->next;
    }

    ListNode *fast = head->next->next, *slow = head;
    while(fast != nullptr && fast->next != nullptr){
        fast = fast->next->next;
        slow = slow->next;
    }
    slow->next = slow->next->next;
    return head;
}

int CountNodeNum(ListNode* head){
    int n = 0;
    while(head != nullptr){
        head = head->next;
        n ++ ;
    }
    return n;
}

ListNode* RemoveNodeByRatio(ListNode* head, int numerator, int denominator){
    if(numerator > denominator || numerator < 1 || head == nullptr){
        return head;
    }

    int n = CountNodeNum(head); // todo：咋这个函数里改变指向，会影响外面的吗？
    int kth = (int) ceil(n * ((double) numerator / (double) denominator));
    if(kth == 1){
        return head->next;
    }
    ListNode *cur = head;
    while(kth != 2){
        cur = cur->next;
        kth --;
    }
    cur->next = cur->next->next;
    return head;
    
}

int run_remove_node_by_ratio(){
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    int numerator = 5, denominator = 7;

    ListNode *head = BuildLinkList(nums);
    PrintLinkList(head);
    ListNode *new_head =  RemoveNodeByRatio(head, numerator, denominator);
    PrintLinkList(new_head);
    return 0;
}

int run_remove_mid_list_node(){
    vector<int> nums = {1, 2, 3};
    ListNode *head = BuildLinkList(nums);
    PrintLinkList(head);
    ListNode *new_head =  RemoveMidListNode(head);
    PrintLinkList(new_head);
    return 0;
}


int run_remove_last_kth_double_node(){
    vector<int> nums = {5, 4, 7, 2, 9};
    ListDoubleNode *head = BuildDoubleLinkList(nums);
    int k = 10;

    PrintDoubleLinkList(head);
    RemoveLastKthDoubleNode(head, k);
    PrintDoubleLinkList(head);

    return 0;
}


int run_remove_lastk_node(){
    vector<int> nums = {5, 4, 7, 2, 9};
    ListNode *head = BuildLinkList(nums);
    int k = 2;

    PrintLinkList(head);
    RemoveLastKthNode(head, k);
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
    // run_remove_lastk_node();
    // run_remove_last_kth_double_node();
    // run_remove_mid_list_node();
    run_remove_node_by_ratio();
    return 0;
    

}