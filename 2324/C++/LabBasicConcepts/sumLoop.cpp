#include <iostream>
#include <string>
using namespace std;

int main(int argc, char** argv) {
  
  int a = stoi(argv[1]);
  int b = stoi(argv[2]);
  
  if (a > b) {
    int c = b;
    b = a;
    a = c;
  }
  
  //add code below this line
  int sum = 0;
  for(a; a <= b; a++){
    sum = sum + a;
  }
  cout << sum << endl;


  //add code above this line
  
  return 0;

}