#include <iostream>

int main() {
    int x,y,xn,yn;
    std::cin >> x;
    std::cin >> y;
    std::cin >> xn;
    std::cin >> yn;
    if ((xn==x) or (yn==y)) {
        std::cout << "YES\n";
    } else if ((xn-x)==(yn-y)) {
        std::cout << "YES\n";
    } else if ((xn-x)==-(yn-y)) {
        std::cout << "YES\n";
    } else {
        std::cout << "NO\n";
    }
    return 0;
} 
