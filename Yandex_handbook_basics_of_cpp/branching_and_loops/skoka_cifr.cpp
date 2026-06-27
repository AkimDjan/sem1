#include <iostream>

int main() {
    unsigned long long int d;
    std::cin >> d;
    int sm=0;
    while (d!=0) {
        sm+=(d%10);
        d/=10;
    }
    std::cout << sm;
    return 0;
}