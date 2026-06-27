#include <iostream>


int main() {
    int month, year;
    char v;
    std::cin >> month >> year;
    if (year%100==0) {
        if (year%400==0) {
            v='y';
        } else {
            v='n';
        }
    } else {
        if (year%4==0) {
            v='y';
        } else {
            v='n';
        }
    }

    //std::cout << month << " " << year << " "<< v <<std::endl;

    if ((month==1) || (month==3) || (month==5) || (month==7) || (month==8) || (month==10) || (month==12)) {
        std::cout<< "31\n";
    } else if ((month==4) || (month==6) || (month==9) || (month==11)) {
        std::cout<< "30\n";
    } else if ((v=='y')&&(month==2)) {
        std::cout<< "29\n";
    } else {
        std::cout<< "28\n";
    }
}