#include <iostream>

void ChangeArrElem(int* arr, int size) {
    std::cout << "arr is new pointer and here is it's address: " << &arr << std::endl;
    if (3 < size) {
        std::cout << "Doing arr[3] = 0;" << std::endl;
        arr[3] = 0;
    }

    int someVar = 5;

    std::cout << "Doing arr = &someVar" << std::endl;
    arr = &someVar;
    std::cout << "*arr = " << *arr << std::endl << std::endl;
}

int main() {
    int var = 8;
    int* p_var = &var;
    std::cout << " p_var = " << p_var << " address of var" << std::endl
        << "*p_var = " << *p_var << " value of var by pointer" << std::endl
        << "&p_var = " << &p_var << " address of pointer p_var" << std::endl << std::endl;
    
    std::cout << "Doing int* p_var2 = &var;" << std::endl;
    int* p_var2 = &var;
    std::cout << " p_var2 = " << p_var2 << " address of var" << std::endl
        << "*p_var2 = " << *p_var2 << " value of var by pointer" << std::endl
        << "&p_var2 = " << &p_var2 << " address of pointer p_var2" << std::endl << std::endl;
    
    
    *p_var2 = 3;
    std::cout << "Doing *p_var2 = 3" << std::endl
        << "var = " << var << std::endl
        << "*p_var = " << *p_var << std::endl
        << " p_var = " << p_var << " var's address isn't changed" << std::endl
        << "&p_var = " << &p_var << " address of pointer isn't changed too" << std::endl << std::endl;

    std::cout << "Doing p_var2 = new int[4] {1, 2, 3, 4};" << std::endl;
    p_var2 = new int[4] {1, 2, 3, 4};
    std::cout << "var = " << var << " var isn't changed" << std::endl
        << "*p_var = " << *p_var
        << " p_var = " << p_var
        << " &p_var = " << &p_var << " p_var isn't changed too" << std::endl;

    std::cout << "But p_var2 now: p_var2 = " << p_var2 << " points to another address" << std::endl
        << "and there is a array: " << std::endl;
    for (size_t i = 0; i < 4; ++i) {
        std::cout << "p_var2[" << i << "] = " << p_var2[i] << " or the same *(p_var2 + " << i << ") = " << *(p_var2 + i) << std::endl;
    }
    std::cout << std::endl;

    std::cout << "Calling ChangeArrElem(p_var2, 4):" << std::endl;
    ChangeArrElem(p_var2, 4);
    std::cout << "We didn't change p_var2 addresses: &p_var2 = " << &p_var2 << " and p_var = " << p_var2 << std::endl;
    std::cout << "But we did change it's values: " << std::endl;
    for (size_t i = 0; i < 4; ++i) {
        std::cout << "p_var2[" << i << "] = " << p_var2[i] << std::endl;
    }
    std::cout << std::endl;
    delete[] p_var2;
    return 0;
}
