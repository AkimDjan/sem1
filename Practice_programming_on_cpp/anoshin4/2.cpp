#include <iostream>


class DinamicArr {

    public:
    size_t capacity;
    size_t size;
    double* arr;
    static const size_t initial_capacity=2;

    DinamicArr() { //constructor
        capacity = initial_capacity;
        size=0;
        arr=new double[capacity];
    }

    DinamicArr(size_t size_, double elem) {
        size=size_;
        arr=new double[size_];
        for (int i=0; i<size ;++i) {
            arr[i]=elem;
        }
    }

    DinamicArr(const DinamicArr& rhs) {
        size=rhs.size;
        capacity=rhs.capacity;
        arr= new double[capacity];
        for (int i=0;i<size;++i) {
            arr[i]=rhs.arr[i];
        }
    }

    ~DinamicArr() { // destructor
        delete[] arr;
    }
    
    void push_back (double l) {
        if (capacity==size) {
            capacity =2;
            double* arr_new=new double[capacity];
            for(int i=0;i<size;++i) {
                arr_new[i]=arr[i];
            }
            delete[] arr;
            arr=arr_new;
        }
        arr[size]=l;
    }

};