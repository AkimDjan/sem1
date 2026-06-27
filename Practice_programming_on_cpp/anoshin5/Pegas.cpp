#include <iostream>



class Horse {
    int hoovesCount=4;
    Horse()
}

class Pegasus: public Horse {
    unsigned int wingscount_;
    public:
        Pegasus(unsigned int hoovesCount; unsigned int wingsCount):
            Horse(hoovesCount);
            wingscount_(wingsCount);

}

void Fly() {
    std::cout<<"I'm flying" <<std::endl;
}

