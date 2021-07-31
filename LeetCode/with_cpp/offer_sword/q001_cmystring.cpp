#include<cstring>

class CMyString
{ //类型CMyString的声明
    public:
        CMyString(char* pData = nullptr); // 这是干啥？
        CMyString(const CMyString& str); // 这又是干啥？
        ~CMyString(void);
    private:
        char* m_pData;
};

// 为CMyString添加赋值运算符函数，经典解法。
CMyString& CMyString::operator=(const CMyString &str)   
//返回值的类型声明为该类型的引用，返回一个引用，才可以允许连续赋值。
// 如果返回值是viod,则不能进行连续赋值，比如str1=str2=str3将不能通过编译。
// 传入的参数的类型也应该声明为常量引用。如果传入的参数不是引用而是实例，那么形参到实参会调用一次复制构造函数。代码效率会降低。
// 赋值运算内不会改变传入的实例状态，因此传入应该有const关键字。
// todo:const 关键字的作用能保护某个变量不变？
// TODO: 复制构造函数不好吗？
{
    if(this == &str)
        return *this; //判断传入的参数和当前的实例*this是不是同一个实例。在释放内存之前要判断是否是同一个，不然就会丢失数据。

    delete []m_pData; //[] 这是在释放内存。在分配新的内存之前释放自身已有空间，防止内存泄露。
    m_pData = nullptr;

    m_pData = new char[strlen(str.m_pData) + 1];    // +1？
    strcpy(m_pData, str.m_pData);

    return *this; //函数结束前返回实例自身的引用（*this）
}

CMyString& CMyString::operator=(const CMyString &str)
{ //为CMyString 添加赋值运算函数，高级方法。
    if (this != &str)
    {
        CMyString strTemp(str);// todo:这是标准库里的？strTemp是干啥的？用于创造临时实例的？
        
        char* pTemp = strTemp.m_pData;
        strTemp.m_pData = m_pData;
        m_pData = pTemp;
    }
    return *this;
}

