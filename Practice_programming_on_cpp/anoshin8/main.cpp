#include <iostream>
#include "Shared_ptr.h"
#include <memory>

class TestClass {
    int value_ = 0;
public:
    TestClass(int value) : value_(value) {
        std::cout << "Constructing" << std::endl;
    }

    ~TestClass() {
        std::cout << "Destructing" << std::endl;
    }

    int GetValue() const {
        return value_;
    }
};

int main() {
    {
        Shared_ptr<TestClass> p1;
        {
            Shared_ptr<TestClass> p2 = MakeShared<TestClass>(5);
            std::cout << p2.GetRefCount() << std::endl;
            p1 = p2;
            std::cout << p1.GetRefCount() << std::endl;
            std::cout << p2.GetRefCount() << std::endl;
        }
        std::cout << p1.GetRefCount() << std::endl;
        std::cout << "Value: " << p1->GetValue() << std::endl;
        std::cout << "Befor delete TestClass obj" << std::endl;
    }
    std::cout << "After delete TestClass obj" << std::endl;
    return 0;
}
