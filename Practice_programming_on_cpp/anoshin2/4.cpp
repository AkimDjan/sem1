#include <iostream>

int main() {
    int i=0, chf1=0, chf2=1, chf=0, k;
    std::cin >> k;
    if (k==0) {
        std::cout << chf1;
    } else if (k==1) {
        std::cout << chf2;
    } else {
        for (i;i<k-1;++i) {
            chf=chf1+chf2;
            chf1=chf2;
            chf2=chf;
        }
        std::cout << chf;
    }
}