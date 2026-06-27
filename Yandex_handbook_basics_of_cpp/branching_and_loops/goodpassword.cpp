#include <iostream>
#include <string>
#include <cctype>


int main() {
    std::string password;
    std::cin >> password;
    int min_len=8, max_len=14;
    if (min_len>password.size() || password.size()>max_len) {
        std::cout << "NO\n";
    }
    int low_c=0, up_c=0, dig_c=0, oth_c=0;

    for ( char string_elem : password ) {
        std::cout << isalnum(string_elem);
        std::cout << islower(string_elem);
        std::cout << isupper(string_elem);
        std::cout << "\n";
    }
}