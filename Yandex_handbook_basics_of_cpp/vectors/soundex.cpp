#include <iostream>
#include <string>

void Append(std::string& neword, char c) {
    if (neword.back() != c) {
        neword.push_back(c);
    }
}

int main() {
    std::string word, neword;
    std::getline(std::cin, word);
    neword.push_back(word[0]);
    for (size_t i=1; i!= word.size();++i) {
        char c = word[i];
        switch (c) {
            case 'b':
            case 'f':
            case 'p':
            case 'v':
                Append(neword, '1');
                break;
            case 'c':
            case 'g':
            case 'j':
            case 'k':
            case 'q':
            case 's':
            case 'x':
            case 'z':
                Append(neword, '2');
                break;
            case 'd':
            case 't':
                Append(neword, '3');
                break;
            case 'l':
                Append(neword, '4');
                break;
            case 'm':
            case 'n':
                Append(neword, '5');
                break;
            case 'r':
                Append(neword, '6');
                break;
        }
    }
    while (neword.size() <4) {
        neword.push_back('0');
    }
    neword.resize(4);
    std::cout << neword << '\n';
}
