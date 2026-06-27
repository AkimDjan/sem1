#include <iostream>

int main() {
    int g;
    std::cin >> g;
    switch (g) {
        case 1:
        case 2:
        case 3:
        case 4:
            std::cout<< "sam gay"<<std::endl;
            break;
        case 12:
            std::cout<< "gay"<<std::endl;
            break;
        default:
            std::cout<< "sosi" << std::endl;
    }
    std::cout << "MyInt:" << g << std::endl;
    return 0;
}