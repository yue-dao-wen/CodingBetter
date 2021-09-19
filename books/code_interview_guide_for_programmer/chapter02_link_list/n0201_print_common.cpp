// # include "datastruct.hpp"
# include "D:\\Efficiency\\50_Zhuanye\\10_Coding\\CodingBetter\\datastruct.hpp"
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

int main(){
    vector<int> nums1 = {1, 2, 3, 4, 5, 6};
    vector<int> nums2 = {0, 2, 3, 4, 7};
    ListNode *head1 = BuildListNode(nums1);
    ListNode *head2 = BuildListNode(nums2);
    PrintCommonValue(head1, head2);
    return 0;

}