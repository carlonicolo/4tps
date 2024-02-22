#include "bicycle.hpp"
#include <iostream>

using namespace std;

Bicycle::Bicycle()
{
    cadence = 0;
    gear = 0;
    speed = 0;
}

Bicycle::Bicycle(int c, int g, int s)
{
    cadence = c;
    gear = g;
    speed = s;
}

void Bicycle::setSpeed(int s){ speed = s; }
int Bicycle::getSpeed(){return speed;}

void Bicycle::changeCadence(int c) { cadence = c; }
void Bicycle::changeGear(int g) { gear = g; }
void Bicycle::speedUp(int inc) { speed += inc; }
void Bicycle::applyBrakes(int dec) { speed -= dec; }

void Bicycle::printStates()
{
    cout << "cadence: " << cadence << "\nspeed:"
         << speed << "\ngear:" << gear << endl;
}

void Bicycle::doubleSpeed()
{
    speed = speed * 2;
    cout << "Bruummm --->>>> " << speed << endl;
}

