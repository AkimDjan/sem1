class Token
{
public:
  char kind;     /// what kind of token
  double value;  /// for numbers: a value

  Token(char ch) : kind{ch}, value{0} {}

  Token(char ch, double val) : kind{ch}, value{val} { ; }
};

class Token_stream
{
public:
  Token_stream();  /// make a Token_stream that reads from cin

  Token get();
  void putback(Token t);

private:
  bool full{false};  /// is there a Token in the buffer?
  Token buffer;      /// here we keep a Token put back using putback()
};
//------------------------------------------------------------
[[noreturn]] inline void error (const string& s)
{
  throw std::runtime_error(s);
}
//------------------------------------------------------------