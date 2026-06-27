#include <iostream>
#include <fstream>
#include <vector>
#include <tuple>
#include <cmath>
#include <string>
#include <iterator>
#include <stdexcept>

struct Point {
    double x, y;

    Point() = default;
    Point(double xx, double yy) : x{xx}, y{yy} {}
};

std::istream& operator >> (std::istream& is, Point& p) {
    return is >> p.x >> p.y;
}

std::ostream& operator >> (std::ostream& os, const Point& p) {
    return os << p.x << " " << p.y;
}

auto read(const std::string& filename) {

    std::ifstream ifs(filename);

    if (!ifs) {
        throw std::runtime_error("Can't open file");
    }

    return std::vector<Point> {
        std::istream_iterator<Point>{ifs},
        std::istream_iterator<Point>{}
    };
}

struct Coeff {
    double value; // value of the coefficient
    double delta; // precision

    Coeff(double value_, double delta_) : value{value_}, delta{delta_}{}
};

auto least_squares_method(const std::vector<Point>& v) {

    const size_t N{v.size()};
    double x_ave{0.0};
    double y_ave{0.0};
    double xy_ave{0.0};
    double x2_ave{0.0};

    for(const auto& p : v) {
        x_ave += p.x;
        y_ave += p.y;
        xy_ave += p.x * p.y;
        x2_ave += p.x * p.x;
    }

    x_ave /= N;
    y_ave /= N;
    xy_ave /= N;
    x2_ave /= N;

    double a{ (xy_ave - x_ave * y_ave) / (x2_ave - x_ave * x_ave) };
    if (!std::isfinite(a))
        throw std::runtime_error("Division by zero");
    
    double b{ y_ave - a * x_ave };
    return std::make_tuple(Coeff{a, 0.0}, Coeff{b, 0.0});
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " file_with_data" << std::endl << argv[1];
        return 2;
    }

    try {
        std::string filename{argv[1]};

        auto [a, b] = least_squares_method(read(filename)); // c++17

        std::cout << "Regression 'y = a * x + b'" << std::endl;
        std::cout << "a = " << a.value << " +- " << a.delta << std::endl;
        std::cout << "b = " << b.value << " +- " << b.delta << std::endl;
        return 0;
    }

    catch(std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
}