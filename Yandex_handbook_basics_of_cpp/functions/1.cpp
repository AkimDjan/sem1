#include <iostream>
#include <string>
#include <vector>
#include "2.h"

int main() {
    std::vector<std::string> parts = {"abra", "ca", "dabra"};
    std::cout << Concatenate(parts) << "\n";  // abracadabra
}