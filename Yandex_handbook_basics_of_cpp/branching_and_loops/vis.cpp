#include <iostream>


int main() {
    int year;
    std::cin >> year;
    if (year%100==0) {
        if (year%400==0) {
            std::cout << "YES\n";
        } else {
            std::cout << "NO\n";
        }
    } else {
        if (year%4==0) {
            std::cout << "YES\n";
        } else {
            std::cout << "NO\n";
        }
    }
}