#include <iostream>

int main() {
    int i=2, k;
    std::cin >> k;
    int a[k-1] ;
    a[0]=0;
    a[1]=1;
    for (i; i<k-1;i++) {
        a[i]=a[i-1]+a[i-2];
    }
    std::cout << a[k];
}