#include <cstdio> // cstdio和stdio啥区别？
#include <stdio.h>
#include <iostream>

bool duplicate(int numbers[], int length, int* duplication)
{
    if(numbers == nullptr || length <= 0)
    {
        return false;
    }

    for (int i = 0; i < length; ++i) // todo: i++ 和 ++i的区别是什么？举一个例子说明区别。
    {
        if (numbers[i] < 0 || numbers[i] > length -1)
        {
            return false;
        }
        
    }

    for (int i = 0; i < length; ++i)
    {
        while (numbers[i] != i)
        {
            if (numbers[i] == numbers[numbers[i]])
            {
                *duplication = numbers[i];
                return true;
            }

            int temp = numbers[i];
            numbers[i] = numbers[temp];
            numbers[temp] = temp;
        }
        
    }
    
    return false;
    
}


bool contains(int array[], int length, int number)
{
    for (int i = 0; i < length; ++i)
    {
        if(array[i] == number)
            return true;
    }
    return false;
}

void test(char* testName, int numbers[], int lengthNumbers, int expected[], int num_expected, bool validArgument)
{
    printf("%s begins:", testName);
    int duplication;
    bool validInput = duplicate(numbers, lengthNumbers, &duplication); 
    if (validArgument == validInput)
    {
        if (validArgument) 
        {
            if (contains(expected, num_expected, duplication))
                printf("Passed.\n");
            else
                printf("FAILED.\n");
        }
        else
            printf("Passed.\n");
    }   
    else
        printf("FAILED.\n");
}

// void test1()
// {
//     int numbers[] = {2, 1, 3, 1, 4};
//     int duplications[] = {1};
//     // const char* name = "Test1";   // 这样就对了吗？或者：char* p=(char*)"hello";
//     char* name=(char*)"Test1";  // 为什么这样就不出问题了？
//     test(name, numbers, sizeof(numbers)/sizeof(int), duplications, sizeof(duplications)/sizeof(int), true);
// }


int main()
{
    int numbers[] = {2, 1, 3, 2, 4};
    int length = sizeof(numbers) / sizeof(int);
    int duplications;
    duplicate(numbers, length, &duplications);
    std::cout << duplications <<std::endl;
    return 0;
}

// int main()
// {
//     test1();
//     return 0;
// }
