#include <iostream>

int fib(int n) {
    int i=2, res;
    int *a=new int[n+1];
    a[0]=0;
    a[1]=1;
    for (i; i<n+1; ++i) {
        a[i]=a[i-1]+a[i-2];
    }
    res=a[n];
    delete[] a;
    return res;
}

int main() {
    int n;
    std::cin >> n;
    std::cout << fib(n);
}