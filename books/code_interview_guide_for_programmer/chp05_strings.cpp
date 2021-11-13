#include<string> // tolearn: 加.h和不加的区别是啥？不加.h才能用string。
#include<iostream>

using namespace std;

class MyString
{
private:
    /* data */
public:
    MyString(/* args */);
    ~MyString();
    bool isDeformation(string str1, string str2);

};

MyString::MyString(/* args */){}
MyString::~MyString() {}

bool MyString::isDeformation(string str1, string str2){
    if(str1.size() != str2.size()) return false;

    int R = 256;    // 这里假设可能出现的字符串都在ascii码中。在面试中，要确认字符串集是什么。
    int map[R]; // 可以用一个变量来初始化长度

    int n1 = str1.size();
    for(int i = 0; i < n1 ; i++){
        map[str1[i]] += 1;
    }

    int n2= str2.size();
    for(int i = 0; i < n2 ; i++){
        map[str2[i]] -= 1;
        if (map[str2[i]] < 0){
            return false;   
            // 如果在str1中出现过，且个数相等，最后会是0；
            // 如果在str1中没有出现过，初始值是0，str2出现的话，就会减1，最后就会负数；
        }
    }

    return true;

}



int main(){

    MyString sl; // c++初始化一个类：类名 变量名;
    bool res = sl.isDeformation("123", "123");
    std::cout << res << std::endl;
    
}