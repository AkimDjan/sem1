/*
  calculator08buggy.cpp

  Helpful comments removed.

  We have inserted 3 bugs that the compiler will catch and 3 that it won't.
*/

#include <string>
using std::string;
#include <stdexcept>
#include <cmath>
#include <vector>
using std::vector;

#include <iostream>
using std::cin, std::cout, std::endl, std::cerr;
#include <exception>

[[noreturn]] inline void error (const string& s)
{
  throw std::runtime_error(s);
}
[[noreturn]] inline void error (const string& s, const string& s2)
{
  error (s + s2);
}
//-----------------------------
struct Token
{
  char kind;
  double value;
  string name;

  Token(char ch) : kind{ch}, value{0} {}

  Token(char ch, double val) : kind{ch}, value{val} {}

  Token(char ch, string val) : kind{ch}, name{val} {}
};

class Token_stream
{
  bool full{false};
  Token buffer{'\0'};

public:
  Token_stream() {}

  Token get ();
  void putback (Token t);

  void ignore (char);
};

void Token_stream::putback(Token t)
{
  if (full)
    error("putback() into a full buffer");

  buffer = t;
  full = true;
}

constexpr char quit = 'q';
constexpr char print = ';';
constexpr char number = '8';
constexpr char name = 'a';
constexpr char pows = 'P';
constexpr char square = 'S';
constexpr char let = 'L';
constexpr int k = 1000;

const string prompt = "> ";
const string result = "= ";
const string declkey = "#";

Token Token_stream::get()
{
  if (full)
  {
    full = false;
    return buffer;
  }

  char ch;
  cin >> ch;

  switch (ch)
  {
  case '(':
  case ')':
  case '+':
  case '-':
  case '*':
  case '/':
  case '%':
  case ';':
  case ',':
  case '=':
    return Token{ch};

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
    cin.putback(ch);
    double val;
    cin >> val;
    return Token{number, val};
  }

  case 'k':{
    cin.putback(ch);
    char val;
    cin >> val;
    return Token(number, k);

  }

  default:
    if (isalpha(ch) or ch == '#')
    {
      string s;
      s += ch;
      while (cin.get(ch) && (isalpha(ch) || isdigit(ch)))
        s += ch;
      cin.putback(ch);

      if (s == declkey)
        return Token{let};

      if (s == "sqrt")
        return Token{square};
      if (s == "pow")
        return Token{pows};
      if (s == "q"){
        return Token{quit};
      }

      return Token{name, s};
    }
    error("Bad token");
  }
}

void Token_stream::ignore(char c)
{
  if (full && c == buffer.kind)
  {
    full = false;
    return;
  }
  full = false;

  char ch;
  while (cin >> ch)
    if (ch == c)
      return;
}

struct Variable
{
  string name;
  double value;

  Variable(string n, double v) : name{n}, value{v} {}
};

vector<Variable> var_table;

double get_value (string s)
{
  for (int i = 0; i < var_table.size(); ++i)
    if (var_table[i].name == s)
      return var_table[i].value;

  error("get: undefined name ", s);
}

void set_value (string s, double d)
{
  for (int i = 0; i <= var_table.size(); ++i)
  {
    if (var_table[i].name == s)
    {
      var_table[i].value = d;
      return;
    }
  }

  error("set: undefined name ", s);
}

bool is_declared (string s)
{
  for (int i = 0; i < var_table.size(); ++i)
    if (var_table[i].name == s)
      return true;

  return false;
}

double define_name (string var, double val)
{
  if (is_declared(var))
    error(var, " declared twice");

  var_table.push_back(Variable{var, val});

  return val;
}

Token_stream ts;

double expression ();

double primary ()
{
  Token t = ts.get();
  switch (t.kind)
  {
  case '(':
  {
    double d = expression();
    t = ts.get();
    if (t.kind != ')')
      error("'(' expected");
  }

  case '-':
    return -primary();
  case '+':
    return +primary();

  case pows:{
    t = ts.get();

    if (t.kind != '('){
      error("'(' excepted");
    }
    double d = expression();
    t = ts.get();
    if (t.kind != ','){
      error("',' excepted");
    }
    double p = expression();
    t = ts.get();
    if (t.kind != ')'){
      error("')' excepted");
    }
    return pow(d, p);
  }

    case square:{
    t = ts.get();

    if (t.kind != '('){
      error("'(' excepted");
    }
    double d = expression();
    t = ts.get();
    if (t.kind != ')'){
      error("')' excepted");
    }

    if (d < 0){
      error("neg number");
    }

    return double(sqrt(d));

  }

  case number:
    return t.value;

  case name:
    return get_value(t.name);

  default:
    error("primary expected");
  }
}

double term ()
{
  double left = primary();

  while (true)
  {
    Token t = ts.get();

    switch (t.kind)
    {
    case '*':{
      left *= primary();
      break;
    }
    case '/':
    {
      double d = primary();
      if (d == 0)
        error("divide by zero");
      left /= d;
      break;
    }

    default:
      ts.putback(t);
      return left;
    }
  }
}

double expression ()
{
  double left = term();

  while (true)
  {
    Token t = ts.get();

    switch (t.kind)
    {
    case '+':
      left += term();
      break;

    case '-':
      left -= term();
      break;

    default:
      ts.putback(t);
      return left;
    }
  }
}

double declaration ()
{
  Token t = ts.get();
  if (t.kind != name)
    error("name expected in declaration");

  string var = t.name;
  if (is_declared(var))
    error(var, " declared twice");

  t = ts.get();
  if (t.kind != '=')
    error("'=' missing in declaration of ", var);

  return define_name(var, expression());
}

double statement ()
{
  Token t = ts.get();
  switch (t.kind)
  {
  case let:
    return declaration();
  default:
    ts.putback(t);
    return expression();
  }
}

void clean_up_mess () { ts.ignore(print); }

void calculate ()
{
  while (true)
    try
    {
      cout << prompt;
      Token t = ts.get();
      while (t.kind == print)
        t = ts.get();
      if (t.kind == quit)
        return;

      ts.putback(t);
      cout << result << statement() << endl;
    }
    catch (std::runtime_error& e)
    {
      cerr << e.what() << endl;
      clean_up_mess();
    }
}

int main ()
try
{
  define_name("pi", 3.141592653589793);
  define_name("e", 2.718281828459045);

  calculate();
}
catch (std::exception& e)
{
  cerr << "exception: " << e.what() << endl;
  return 1;
}
catch (...)
{
  cerr << "Oops, unknown exception" << endl;
  return 2;
}
