#include <iostream>
namespace my
{
    int x=0;
    int cout = 789;
    int vector =111;
    namespace sub
    {
        int y=321;
    };
};
int x=0;

int main() 
{
    int x=123;
    std::cout << x <<"\n";
    {
        int x=456;
        std::cout << x << "\n";
    }
    std::cout << x << "\n";
    std::cout << my::x << my::sub::y<< std::endl;
    return 0;
}