#include "bicycle.hpp"
#include <iostream>

int main()
{
    // Create two different Bicycle objects
    Bicycle bike1;
    Bicycle bike2;
    Bicycle bike3(50, 100, 500);
    // Invoke methods on those objects
    bike1.changeCadence(50);
    bike1.speedUp(10);
    bike1.changeGear(2);
    bike1.printStates();
    bike2.changeCadence(40);
    bike2.speedUp(20);
    bike2.changeGear(3);
    bike2.printStates();
    bike2.setSpeed(100);
    bike2.printStates();

    std::cout << "\n--- bike3 ---" << std::endl;
    bike3.printStates();
    bike3.doubleSpeed();
}