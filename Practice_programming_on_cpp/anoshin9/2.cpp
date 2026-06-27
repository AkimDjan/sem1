#include <stdexcept>
#include <iostream> 
#include <memory>

class OurExcept: public std::runtime_error 
{
    public:
        OurExcept() : std::runtime_error("OurExcept!!! "){};
};

class SomeClass
{
    public:
        ~SomeClass() { 
            std::cout << "Destructor" << std::endl;
            }

};

int main() {
    try {
        std::unique_ptr<SomeClass> sc = std::make_unique<SomeClass>();
        throw 1;
    } catch(const OurExcept& oe) {
        std::cout << "OurException: " << oe.what() << std::endl;
    } catch(const std::exception& e) {
        std::cout << "exception: " << e.what() << std::endl;
    } catch(...) {
        std::cout<< "...:"<< std::endl;
    }
    return 0;
}

