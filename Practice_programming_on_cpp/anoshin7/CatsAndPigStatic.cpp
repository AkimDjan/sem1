#include <iostream>

class Cat {
public:
    void Sound() { std::cout << "Purr" << std::endl; }
};

class Pig {
public:
    void Sound() { std::cout << "Oink" << std::endl; }
};

template <class T>
void Sound(T animal) { animal.Sound(); }

int main() {
    Cat cat;
    Pig pig;
    Sound(cat);
    Sound(pig);
    return 0;
}
