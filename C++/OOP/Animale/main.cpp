#include "animale.hpp"
#include <iostream>
#include <string>

using namespace std;

int main()
{
    Animale jimmy();
    Animale billy("Billy", 20, 4);

    string name = billy.getNome();
    cout << "Nome ---> " << name << endl; 
}