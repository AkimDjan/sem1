#include <iostream>

//ШАБЛОНЫ

template <class T> //template инициализирует шаблон
T fun(T x, T y) {
    return x / y;
}

int main() {
    std::cout << fun(3,2) << std::endl;
    std::cout << fun(3.0,2.0) << std::endl;
    std::cout << fun('3','2') << std::endl;
    return 0;
    int* p = new int;
}