#include <iostream> 
#include <string>

int main() {
    std::string stroka, drugaya, bezprobelstroka;
    std::getline(std::cin, stroka);
    for (int i = stroka.size()-1; i!=-1; --i) {
        if (stroka[i] != ' ') {
            drugaya.push_back(stroka[i]);
        }
    }
    for (int i=0; i != stroka.size(); ++i) {
        if (stroka[i] != ' ') {
            bezprobelstroka.push_back(stroka[i]);
        }
    }
    if (bezprobelstroka == drugaya) {
        std::cout << "YES\n";
    } else {
        std::cout << "NO\n";
    }
}