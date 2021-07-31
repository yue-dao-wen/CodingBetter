#include<string>
#include<iostream>
using namespace std;

class Solution {
public:
    int titleToNumber(string columnTitle) {
        int ans = 0;   
        long multi = 1;

        for (int i = columnTitle.size()-1; i >=0 ; i--){
            int num = columnTitle[i] - 'A' + 1;
            ans += multi * num;
            multi *= 26;
        }
        return ans;
    }
};

int main(){
    // string str = "ABC";
    string str = "ZY";
    Solution* sl = new Solution();
    int ans = sl->titleToNumber(str);
    std:cout<< ans << std::endl;
}