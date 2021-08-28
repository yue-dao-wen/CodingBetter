#include <math.h>
#include<vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int compress_learn1(vector<char>& chars){
        int write = 0, left = 0;
        int n = chars.size();
        for(int read=0; read < n; read++){
            if(read == n-1 || chars[read] != chars[read+1]){
                chars[write++] = chars[read];
                int cnt = read - left + 1;
                if(cnt > 1){
                    int write_bcup = write;
                    while(cnt > 0){
                        chars[write++] = cnt % 10 + '0';
                        cnt /= 10;

                    }
                    reverse(&chars[write_bcup], &chars[write]);
                }
                left = read + 1;
            }
        }
        return write;
    }

    int compress(vector<char>& chars) {
        int left=0, right=0, ans=0;
        int n = chars.size();
        int cnt = 0;
        int next_idx = 0;
        while(right < n){
            while(right < n && chars[right] == chars[left]){
                cnt ++;
                right ++;
            }
            if(cnt == 1){
                cnt = 0;
                left ++;
                right = left;
                ans ++;
                continue;
            }
            left ++;
            int n_digit = 0;
            while(cnt / pow(10, n_digit) != 0){
                n_digit ++;
            }
            int cur_num;
            char cur_num_char;
            while(n_digit != 0){
                cur_num = cnt / pow(10, n_digit-1);
                cur_num_char = '0' + cur_num;
                chars[left] = cur_num_char;
                left ++; // 能先++,再赋值吗？
                n_digit --;
                ans ++;
            }
            left = right;
            cnt = 0;
        }
        return ans;
    }
};