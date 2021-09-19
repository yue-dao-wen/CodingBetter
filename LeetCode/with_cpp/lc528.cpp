// C++STL说明：

// mt19937头文件是<random> 是伪随机数产生器，用于产生高性能的随机数
// uniform_int_distribution 头文件在<random>中，是一个随机数分布类，参数为生成随机数的类型，构造函数接受两个值表示区间段
// accumulate 头文件在<numeric>中，求特定范围内所有元素的和。
// spartial_sum函数的头文件在<numeric>，对(first, last)内的元素逐个求累计和，放在result容器内
// back_inserter函数头文件<iterator>，用于在末尾插入元素。
// lower_bound头文件在<algorithm>，用于找出范围内不大于num的第一个元素

class Soluiton{
private:
    mt199937 gen;
    uniform_int_distribution<int> dis;
    vector<int> pre;
public:
    Solution(vector<int>& w): gen(random_device{} ()), di

}