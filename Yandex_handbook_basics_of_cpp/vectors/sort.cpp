#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> lines;

    std::string line;
    while (std::getline(std::cin, line)) {
        lines.push_back(line);
    }

    std::sort(lines.rbegin(), lines.rend());

    for (size_t i = 0; i != lines.size(); ++i) {
        std::cout << lines[i] << "\n";
    }
}