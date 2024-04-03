#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

class Rectangle
{
public:
    Rectangle()
    {
        nomeFigura = "Rettangolo";
        height = 10;
        width = 5;
    }

    Rectangle(string n_nomeFigura, int n_height, int n_width)
    {
        nomeFigura = n_nomeFigura;
        height = n_height;
        width = n_width;
    }

    int getArea()
    {
        return (width * height);
    }

    int computePerimeter()
    {
        return (2 * (width + height));
    }

    string getNomeFigura()
    {
        return nomeFigura;
    }

private:
    int width;
    int height;
    string nomeFigura;
};

int main()
{
    std::ifstream myfile;
    myfile.open("objects.txt");
    std::string myline;

    int sentinelValue = 0;
    int objectNumber = 0;

    vector<std::string> vecOfStrs;
    vector<Rectangle> vecOfRectangle;

    if (myfile.is_open())
    {
        while (myfile)
        { // equivalent to myfile.good()
            objectNumber++;
            while (sentinelValue < 3)
            {
                std::getline(myfile, myline);
                std::cout << myline << '\n';
                vecOfStrs.push_back(myline);
                sentinelValue++;
                std::cout << "sentinelValue: " << sentinelValue << std::endl;
            }

            std::cout << "Oggetto #" << objectNumber << endl;
            sentinelValue = 0;

            Rectangle a(vecOfStrs[0], stoi(vecOfStrs[1]), stoi(vecOfStrs[2]));
            vecOfStrs.clear();
            vecOfRectangle.push_back(a);
        }

        // rimuovo ultimo elemento vector
        vecOfRectangle.pop_back();

        cout << "\nList of objects in vecOfRectangle vector: " << endl;

        for (Rectangle i : vecOfRectangle)
        {
            cout << i.getNomeFigura() << endl;
        }
    }
    else
    {
        std::cout << "Couldn't open file\n";
    }
    return 0;
}