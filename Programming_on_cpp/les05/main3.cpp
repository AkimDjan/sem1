#include <iostream>


int main() {
    int n=123;
    int A[n]={42, 66, 77};
    int* p =A;

    std::cout <<A[0]<< " "<<A[9]<<std::endl;
    std::cout << *p++ << " "<< *p++ << std::endl;
    return 0;
}