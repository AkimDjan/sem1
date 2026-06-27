#include <iostream>


class A {
    int a=5; // private по умолчанию, а в strusct (вместо class) все поля по умолчанию public
    public:
    A() { a=6;// конструктор 
        std::cout << "Constructing" << "\n"; // A* a; - конструктор не вызовется
    }
    ~A() {std::cout << "destructing"<< "\n";} //деструктор
    A(int a_): a(a_){
        std::cout <<"constructing"<< "\n";
    }
    void Print(int b) {
    std::cout<<b<<"\n";
    }
    void Print() {
    std::cout<<this<<"\n";
    }
    /* A( const A& rhs): a(rhs,a) {
        std::cout<<"constructing"<<"\n";   
    }
    A& operator=(const A& rhs) {
        if (this==&rhs) {
            return *this
        }
        delete[] a 
        a=new int[rhs.size]
        for (size_t i=0; i<size; ++i) {
            a[i]=rhs.a[i]
        }

    } return this */
};



int main() {
    A* a=nullptr;
    a=new A();
    a -> Print();
    
    
    std::cout<<"Goodbye"<<std::endl;
    delete a;
    return 0;
}
