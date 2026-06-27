#include <iostream>

int main() {
    int a,b,c;
    std::cin >> a;
    std::cin >> b;
    std::cin >> c;
    if ((a+b>c)&&(a+c>b)&&(c+b>a)) {
        if ((a*a + b*b == c*c) || (c*c + b*b == a*a) || (a*a + c*c == b*b)) {
            std::cout << "YES\n";
        } else {
            std::cout << "NO\n";
        }
    } else {
        std::cout << "UNDEFINED\n";
    }
}