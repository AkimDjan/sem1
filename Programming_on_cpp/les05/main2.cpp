#include <iostream>

void f(int& x)
{
    x= x + 1;
}

int main() {
    int a=42;
    f(a); // {int *x = &a; *x = * x+ 1}

    int& r=a;


    std::cout << a << std::endl;
    return 0;
}