/** Least Squares method
 * (x,y)... -> y=ax+b
 * a=<y> - b<x>; b=(<x*y> - <x>*<y>)/(<x*x>-<x>*<x>)
 * <f>= (сумма fi)/N
 *
 */ 

#include <cmath>
#include <fstream>
#include <iostream>
#include <vector>
#include <iterator>

struct Point
{
    double x,y;

    Point() : x(NAN), y(NAN) { ; }
    Point(double _x, double _y): x(_x), y(_y) { ; }
};

std::istream& operator>>(std::istream& is, Point& p) // ? почему работая с операторами мы используем ссылки?
{
    return is >> p.x >> p.y;
    /* std::istream& is1 = is.operator>>(p,x);
    std::istream& is2 = is1.operator>>(p,y);
    return is2;  на низком уровне */
}

std::ostream& operator<<(std::ostream& os, Point& p) 
{
    return os << p.x << " " << p.y;

}
//--------------------------

/** Функция для чтения точек из файла 
 * 
 * @param[in] filename - имя файла
 * 
 * @return вектор точек
 */

std::vector<Point> read_data(const std::string& filename)
{
    std::ifstream ifs(filename); /*Input File STREAM*/
    if ( ! ifs.is_open() ) {
        throw std::runtime_error("Error opening file: " + filename);
    }
    /*std::istream_iterator<Point> begin(ifs);
    std::istream_iterator<Point> end;
    std::vector<Point> d{begin,end};*/
    std::vector<Point> vec{std::istream_iterator<Point>(ifs),std::istream_iterator<Point>()};
    return vec;
}
//-------------------------------------------

struct Coeff
{
    double value;
    double delta; //confidence bad - доверительный диапазон
    //Coeff()=delete; //default
    Coeff(double _v, double _d) : value{_v}, delta{_d} { ; }
};
//--------------------------------------------

/**
 * Метод наименьших квадратов
 */
std::tuple<Coeff,Coeff> least_squares(const std::vector<Point>& points) 
{
    size_t N=points.size();
    double avgX=0.0, avgY=0.0, avgXX=0.0, avgXY=0.0;

    /* (1)
    for (int i=0;i<N;++i) 
    {
        const Point& p=points[i]
        // ...
    }
    */

    /* (2)
    for(std::vector<Point>::const_iterator i=point.begin(); i!=points.end(); ++i)
    {
        const Point& p = *i;
        //...

    }
    */

    for(const Point& p : points)
    {
        avgX +=p.x; //avgX = avgX + p.x
        avgY +=p.y;
        avgXY += p.x*p.y;
        avgXX += p.x*p.x;


    }
    avgX /= N;
    avgY /= N;
    avgXY /= N;
    avgXX /= N;

    double b = (avgXY - avgX * avgY) / (avgXX - avgX * avgX);
    if (!std::isfinite(b)) {
        throw std::overflow_error("Bad slopes coefficient. Divizion by zero");
    }
    double a = avgY - b * avgX;

    return std::make_tuple(Coeff(a,0.0), Coeff(b,0.0));

}


int main(int argc, char* argv[]) 
{
    if (argc!=2) {
        std::cerr << "Usage: " << argv[0] << " FILE_WITH_XY_DATA";
        return 1;
    }
    try {
        std::string filename = argv[1];
        std::vector<Point> points= read_data(filename);
        auto [a,b] = least_squares(points);
        std::cout << filename << ": a=" << a.value <<"; b="<< b.value<<std::endl;

    }
    catch (std::exception& e) {
        std::cerr <<"Error: "<< e.what();
    }


}
//-------------------------------------------------