#include <string>
#include <iostream>



bool IsGood(const std::string& password) {
    if (password.size() < 8 || password.size() > 14) {
        return false;
    }
    int upper=0;
    int lower=0;
    int digit=0;
    int other=0;

    for (char c : password) {
        if ('A'<= c && c<= 'Z') {
            upper = 1;
        } else if ('a'<= c && c<= 'z') {
            lower = 1;
        } else if ('0'<= c && c<= '9') {
            digit = 1;
        } else {
            other = 1;
        }
    }
    return upper+lower+digit+other>=3;
    
}

int main() {
    std::string password;
    std::getline(std::cin,password);
    if (IsGood(password)) {
        std::cout << "YES\n";
    } else {
        std::cout << "NO\n";
    }
}
