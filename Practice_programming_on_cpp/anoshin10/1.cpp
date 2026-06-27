#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> a;
    for (int i = 0; i < 3; ++i) {
        int n = 0;
        std::cin >> n;
        a.push_back(n);
    }
    std::sort(a.begin(), a.end());

    /*
     * for (auto el: cont) есть копирование
     * for (auto& el: cont) нет копирования, можем менять элемент
     * for (const auto& el: cont) нет копирования, но и не можем менять элементы
     */
    for (auto x: a)
        std::cout << x << " ";
    return 0;
}