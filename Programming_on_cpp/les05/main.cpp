#include <iostream>
#include <math.h>
#include <cmath>

int main() 
{
    int a=26;
    int* p=&a;
    float* pf = reinterpret_cast<float*>(&a);
    char* pc = reinterpret_cast<char*>(&a);

    double b = (double) 3/2;

    

    std::cout << "Addr a=" << &a  << std::endl;
    std::cout << "value p=" << *p  << std::endl;
    std::cout << "value pf=" << *pf  << std::endl;
    std::cout << "value pc=" << *pc  << std::endl;
    std::cout << "value b=" << b << std::endl;


    *p=66;
    std::cout << "value p=" << *p  << std::endl;
    std::cout << "Value a=" << a  << std::endl;

    return 0;
}