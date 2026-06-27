#include <iostream>

int main() {
    int n;
    std::cin >> n;
    double* matrix = new double[9] {
        1, 1, 1,
        3, 4, 5,
        2, 2, 2
    };
    for (int i=0 ; i<n ;++i) {
        for (int j=0 ; j<n ; ++j) {
            std::cout << matrix[i*n+j] << " ";
        } 
        std::cout  << "\n";
    }
    return 0;
}