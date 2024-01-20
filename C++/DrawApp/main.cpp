#include <iostream>
using namespace std;

void forLoopAnnidato(int numStars, char typeOfStarts)
{
  for(int i=0; i <= numStars; i++)
  {
    cout << "" << endl;
    for(int j=0; j < i; j++)
    {
      cout << typeOfStarts ;
    }
  } 
}

int main() {
  forLoopAnnidato(11, '*');
}
