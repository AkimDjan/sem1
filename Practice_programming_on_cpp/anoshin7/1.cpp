#include <iostream>

class Base {
    public:
        void fun() const {
            std::cout<< "Base"<< std::endl;
        }
        virtual ~Base() {};
};

class Derived: public Base {
    public: 
        void fun() const {
            std::cout<<"Derived"<<std::endl;
        }
};

int main() {
    /*Base b;
    Derived d;
    b.fun();
    d.fun();
    d.Base::fun();*/
    Base* pb = new Base();
    pb->fun();
    Derived* pd = new Derived();
    pd->fun();
    delete pb, delete pd;



    return 0;
}