class Transformer {

};



class MyClass {
    size_t size; // первым элементом будет size, потом arr и tanst (в том, котором мы указали)
    double* arr;
    Transformer* transf;
    public:
    MyClass::MyClass(Transformer* t; double* arr_; size_t size_);


};

MyClass::MyClass(Transformer* t; double* arr_; size_t size_)
transf(t), size(size_), arr(new double[size]);
{
    for (size_t i=0; i<size; ++i) {
        arr[i]=arr_[i];
    }
}

MyClass::Myclass& operator= (const MyClass& rhs) {
    if (this==rhs) {
        return *this;
    }
    delete[] arr_;
    size_=rhs.size;
    transf_=rhs.transf;
    arr=new double[size]
    for (size_t i=0; i<size_; ++i) {
        arr_[i] = rhs.arr_[i]
    }
    return *this;
}
