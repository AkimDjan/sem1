#include <iostream>

double determin(double* matrix, int matrix_size) {
    for (int i = 0; i < matrix_size; i++) {
        for (int j = i + 1; j < matrix_size; j++){
            int koef; 
            koef = matrix[j*matrix_size + i] / matrix[i*matrix_size + i];
            for (int k = i; k < matrix_size; k++) {
                matrix[j*matrix_size + k] -= koef*matrix[i*matrix_size + k];
            }
        }
    }
    int det = 1;
    for (int m = 0; m < matrix_size; m++){
        det *= matrix[(matrix_size+1)*m];
    }
    delete[] matrix;
    return det;
}

int main() {
    int matrix_size;
    double* matrix = new double[matrix_size * matrix_size];
    std::cout << "Размер матрицы: " << "\n";
    std::cin >> matrix_size;
    std::cout << "Элементы матрицы: " << "\n";
    for (int i = 0; i < matrix_size * matrix_size; ++i) {
        std::cin >> matrix[i];
    }
    std::cout << "Определитель: " << determin(matrix, matrix_size) << "\n";
    return 0;
};