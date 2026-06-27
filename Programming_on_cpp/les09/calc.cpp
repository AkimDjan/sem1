//
// This is example code from Chapter 6.7 "Trying the second version" of
// "Software - Principles and Practice using C++" by Bjarne Stroustrup
//

/*
  This file is known as calculator02buggy.cpp

  I have inserted 5 errors that should cause this not to compile
  I have inserted 3 logic errors that should cause the program to give wrong
  results

  First try to find and remove the bugs without looking in the book.
  If that gets tedious, compare the code to that in the book (or posted
  source code)

  Happy hunting!

*/


//#include <std_lib_facilities.h>

#include <string>
using std::string;
#include <stdexcept>

#include <iostream>
using std::cin, std::cout;
#include <exception>
#include "defsh"

Token_stream ts;

int main ()
try{ 
  double val=0.0; // NAN
  while (cin)
  {
    Token t = ts.get();
    

    if (t.kind == 'q')
      break;            // 'q' for quit
    if (t.kind == ';')  // ';' for "print now"
      cout << "=" << val << '\n';
    else
      ts.putback(t);

    val = expression();
  }
}
catch (std::exception& e)
{
  std::cerr << "error: " << e.what() << '\n';
  return 1;
}
catch (...)
{
  std::cerr << "Oops: unknown exception!\n";
  return 2;
}