# include <iostream>
#include <tchar.h>  // todo: 这是啥？

int GetSize(int data[])
{
    return sizeof(data);    
// 原因是数组作为参数传给函数时，是传给数组的地址，而不是传给整个的数组空间，因而
// sizeof(arr)这句话会报错
// 正确的用法是：不在函数内部使用sizeof
}

int main(int argc, _TCHAR* argv[])
{
    int data1[] = {1, 2, 3, 4, 5};  // data1是数组，求数组的大小。一个整数4字节，5个就是20字节。
    int size1 = sizeof(data1);

    int *data2 = data1; // data2是一个指针，地址，指向了第一个数字，本质是指针。对任意一个指针求sizeof都是4.
    int size2 = sizeof(data2);

    int size3 = GetSize(data1); // 当数组作为函数参数传递时，数组退化为同类型的指针，指向int的指针，所以还是4.

    printf("%d, %d, %d", size1, size2, size3);
    return 0;
}

