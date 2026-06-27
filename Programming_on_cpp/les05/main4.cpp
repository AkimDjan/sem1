#include <iostream>


void f(int* _p) 
{
    delete[] _p;
}

int main() {

    int** p =new int*[10];
    for(int i=0; i<10;++i) {
        *p=new int[42]
    }
    int* A=new int[420]
    int*** p=A;
    std::cout << *p++ << " " << *p++ << std::endl;

    int* ppp=p;
    delete[] p; p =nullptr;
    p[0]=42;
    return 0;
}