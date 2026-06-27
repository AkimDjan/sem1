#include <string>
using std::string;
#include <stdexcept>

#include <iostream>
using std::cin, std::cout;
#include <exception>
#include "defs.h"

Token_stream::Token_stream() : buffer{0}  /// no Token in buffer
{
}

void Token_stream::putback(Token t)
{
  if (full)
    error("putback() into a full buffer");

  buffer = t;
  full = true;
}

Token Token_stream::get()
{
  if (this->full)  // do we already have a Token ready?
  {
    full = false;  // remove Token from buffer
    return buffer;
  }

  char ch;
  cin >> ch;  // note that >> skips whitespace (space, newline, tab, ...)

  switch (ch)
  {
  case ';':  // for "print"
  case 'q':  // for "quit"
  case '(':
  case ')':
  case '+':
  case '-':
  case '*':
  case '/':
    return Token{ch};  // let each character represent itself

  case '.':
  case '0':
  case '1':
  case '2':
  case '3':
  case '4':
  case '5':
  case '6':
  case '7':
  case '8':
  case '9':
  {
    cin.putback(ch);  // put digit back into the input stream
    double val;
    cin >> val;              // read a floating-point number
    return Token{'8', val};  // let '8' represent "a number"
  }

  default:
    error("Bad token");
  }
}



double expression ();

/// deal with numbers and parentheses
double primary ()
{
  Token t = ts.get();
  switch (t.kind)
  {
  case '(':  // handle '(' expression ')'
  {
    double d = expression();
    t = ts.get();
    if (t.kind != ')')
      error("')' expected");
    return d;
  }

  case '8':  // we use '8' to represent a number
    return t.value;

  default:
    error("primary expected");
  }
}

/// deal with *, /, and %
double term ()
{
  double left = primary();
  Token t = ts.get();  // get the next token from token stream

  while (true)
  {
    switch (t.kind)
    {
    case '*':
      left *= primary();
      t = ts.get();
      break;
      //[[passthrough]] подсказка компилятору что break не поставлен намеренно

    case '/':
    {
      double d = primary();
      if (d == 0)
        error("divide by zero");
      left /= d;
      t = ts.get();
      break;
    }

    default:
      ts.putback(t);  // put t back into the token stream
      return left;
    }
  }
}

/// deal with + and -
double expression ()
{
  double left = term();  // read and evaluate a Term
  Token t = ts.get();    // get the next token from token stream

  while (true)
  {
    switch (t.kind)
    {
    case '+':
      left += term();  // evaluate Term and add
      t = ts.get();
      break;

    case '-':
      left -= term();  // evaluate Term and subtract
      t = ts.get();
      break;

    default:
      ts.putback(t);  // put t back into the token stream
      return left;    // finally: no more + or -: return the answer
    }
  }
}