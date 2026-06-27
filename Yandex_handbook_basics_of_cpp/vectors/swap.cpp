#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> seats(n);
    for (int guest = 1; guest <= n; ++guest) {
        int seat;
        std::cin >> seat;
        seats[seat - 1] = guest;
    }

    for (int guest : seats) {
        std::cout << guest << " ";
    }
    std::cout << "\n";
}