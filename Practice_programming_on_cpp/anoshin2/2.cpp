#include <iostream>

int main() {
    int a=0;
    int* pa=&a;
    char ch='a';
    char* pch=&ch;
    std::cout << sizeof(a) <<"\n";
    std::cout << sizeof(ch) <<"\n";
    std::cout << sizeof(pa) <<"\n";
    std::cout << sizeof(pch) <<"\n";
}
