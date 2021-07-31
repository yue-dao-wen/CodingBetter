#include <iostream>

int countRange(int* numbers, int length, int start, int middle)  // 为什么要加上const?
{
    if (numbers == nullptr || length == 0)
    {
        return 0;
    }
    
    int count = 0;
    for (int i = 0; i < length; i++)
    {
        if (start <= numbers[i] && numbers[i] <= middle)
        {
            count ++;
        }
    }
    return count;
}

int getDuplication(int* numbers, int length)
{
    if (numbers == nullptr || length == 0)  // 有没有可能numbers是空指针，但是长度不为0？
        return -1;

    int start = 0;
    int end = length - 1;
    while (end >= start)
    {
        int middle = start + ((end - start) >> 1);
        int count = countRange(numbers, length, start, middle);
        std::cout << count << std::endl;
        if (end == start)
        {
            if(count > 1) return end;
            else break; // 没有重复
        }
        if (count > (middle - start + 1))
            end = middle;
        else
            start = middle + 1;
    }
    return -1;
}


int main()
{
    int numbers[] = {2, 3, 1, 0, 2, 5, 3}; // todo: 数组定义这么做？
    int length = sizeof(numbers) / sizeof(int);
    int duplication = getDuplication(numbers, length);
    // printf("%d", duplication);
    // std::cout << "the duplication is " << duplication << " ." << std::endl;
    std::cout << duplication << std::endl;
    return 0;
}