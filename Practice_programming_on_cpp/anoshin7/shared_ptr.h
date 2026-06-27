#include <iostream>
#pragma once //директива препроцессору  

template <class T>
class Shared_ptr{
    T* pointer=nullptr;
    size_t* reference_count = nullptr;
    public:
    Shared_ptr(const T& obj) {
        pointer = new T (obj);
        reference_count = new size_t(1);
    }
    Shared_ptr(const Shared_ptr<T>& rhs) {
        pointer = rhs.pointer;
        reference_count = rhs.reference_count;
        ++(*reference_count);
    }
    ~Shared_ptr() {
        --(*reference_count);
        if (!(*reference_count)) {
            delete pointer;
            delete reference_count;
        }
    }
    Shared_ptr<T>& operator=(const Shared_ptr<T>& rhs) {
        if (this==rhs) {
            return *this;
        }
        --(*reference_count);
        if (!(*reference_count)) {
            delete pointer;
            delete reference_count;
        }
        reference_count=rhs.reference_count;
        pointer=rhs.pointer;
        ++(*reference_count);
    }
    /*Shared_ptr<T>& operator>>(const Shared_ptr<T>& rhs) {
    
    }*/

};
