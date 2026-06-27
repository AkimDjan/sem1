#include <iostream>

int main( int argc, char* argv[]) {

    for(int i = 0; i < argc; ++i) {
        std::string value= argv[i];
        std::cout << "Arg #" << i << ": " << argv[i] << std::endl;
        if (value == "--help" || value == "-h") {
            std::cout<< "Usage: " << argv[0] << " [--help] [ARG1 ARG2 ...]" << std::endl;
            return 0;
        }
    }
    if (std::string(argv[1]) == "--help") {
    }
    return 0;
}