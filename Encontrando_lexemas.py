def counting_lexemes(code, lexeme):
  # Complete esse código
  i = 0;
  n = code.find(lexeme, i)
  count = 0
  while n != -1:
    n = code.find(lexeme, n+1)
    count = count + 1
  return count

code = code = """
int main(){
  int a1, a2;
  a1 = a1 + 2;  
  a2 = a1 + 5;  
}
"""
assert ( counting_lexemes(code, "a1") == 4 )

code = input()
lexeme = input()
print ( counting_lexemes(code, lexeme))
