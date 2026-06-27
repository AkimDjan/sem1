#include <iostream>
#include <cmath>


int main() 
{
    double n;
    std::cin >> n;
    double ln2=0;
    for (int i=1; i<=n; ++i) {
        ln2+=pow(-1,i+1)/i;
    }
    std::cout << ln2;

    return 0;

}