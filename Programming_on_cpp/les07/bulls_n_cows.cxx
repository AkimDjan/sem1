/**
 * Bulls and cows program
 * 
 * @author Akim Tarasov
 */

// можно использовать 3 слэша

#include <iostream>
#include <vector>
#include <stdint.h>
#include <stdlib.h>
#include <string>
//#include <random>

const int DIGIT_COUNT=4;
using Number=std::vector<char>;

//std::vector<uint8_t>   number; // '0', '1', '2', '3', ... , '9'
//std::array<uint8_t, 4> number;
//using number_t=std::vector<char>;
std::ostream& operator<<(std::ostream& os, Number& n)
{
    for (char c:n) {
        os<<c;
    }
    return os;
}

//Number comp_number = {'1', '2', '3', '4'};
//----------------------------------------------

//Forward declarations
Number rand_number();
Number user_guess();
bool validate_number(const Number& num);
int count_cows(char digit, const Number& num) ;
//----------------------------------------------
Number rand_number()
{
    Number res(DIGIT_COUNT);
    do{
        for (int i=0; i<DIGIT_COUNT; ++i)
        {
            res[i] = '0' + int(rand()/double(RAND_MAX)*10);

        }
    } while (! validate_number(res) );

    return res;
}
//----------------------------------------------
/**
 * Функция чтения числа со стандартного ввода с клавиатуры
 * 
 * @return массив цифр
 */
Number user_guess()
{   
    Number res={'-','-','-','-'};
    std::cout << "Enter your guess: ";
    for(int i=0; i<DIGIT_COUNT; ++i) {
        std::cin >> res[i];
    }
    
    if (! std::cin || ! validate_number(res)) {
        std::cerr << "*ERR:Wrong input" << std::endl;
        return res;
    }
    
    return res; 
}
//----------------------------------------------
/**
 * Считает число "коров" (есть ли цифра в заданном числе не на своем месте)
 * @param digit цифра для поиска 
 * @param num  число, в котором искать цифру
 * 
 * @return число вхождений цифры в числе
 */
int count_cows(char digit, const Number& num) 
{   
    int cc=0;
    for (char c: num)
    {
        if (digit==c){
            ++cc;
        }
    }
    return cc;
}
//------------------------------------
bool validate_number(const Number& num)
{   

    for(char c:num) {
        if ( ! std::isdigit(c) ) {
            std::cerr << "Only digits allowed (0 .. 9)"<< std::endl;
            return false;
        }

        if (count_cows(c, num)!= 1)
        {
            std::cerr <<"*ERR: Digits should be unique";
            return false;
        }
    }
    return true;
}
//------------------------------------
int main()
{   
    Number comp_number = rand_number();
    int bulls=0, cows=0;
    do {
        bulls=0; cows=0;
        Number user_number = user_guess();
        std::cout << user_number << std::endl;
        for (int i=0; i<user_number.size();++i)
        {
            if(user_number[i]==comp_number[i]) 
            {
                ++bulls;
            } else if (count_cows(user_number[i], comp_number)==1) 
            {
                ++cows;
            }
        }
        std::cout<<"Bulls: "<< bulls << ", Cows:" << cows << std::endl;
    } while (bulls != comp_number.size());
    std::cout<<"Congrats!"<<std::endl;

    return 0;
}

