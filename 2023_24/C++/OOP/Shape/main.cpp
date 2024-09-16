#include <iostream>

using namespace std;

// Base class
class Shape {
   public:
      // pure virtual function providing interface framework.
      virtual int getArea() = 0;
      virtual int computePerimeter() = 0;
      void setWidth(int w) {
         width = w;
      }

      void setHeight(int h) {
         height = h;
      }

      int getWidth(){
          return width;
      }

      int getHeight(){
          return height;
      }

   protected:
      int width;
      int height;
};

// Derived classes
class Rectangle: public Shape {
   public:
      int getArea() { 
         return (width * height); 
      }

      int computePerimeter(){
          return ((width + height)*2);
      }
};

class Triangle: public Shape {
   public:
      int getArea() { 
         return (width * height)/2; 
      }

      int computePerimeter(){
          return (width + cateto1 + cateto2);
      }

      int cateto1 = 5;
      int cateto2 = 5;
};


int main(void) {
  try {
    
     Rectangle Rect;
     Triangle  Tri;
  
     Rect.setWidth(5);
     Rect.setHeight(7);
  
     // Print the area of the object.
     cout << "Total Rectangle area: " << Rect.getArea() << endl;
     cout << "Perimeter: " << Rect.computePerimeter() << endl;
  
     Tri.setWidth(5);
     Tri.setHeight(7);
  
     // Print the area of the object.
     cout << "Total Triangle area: " << Tri.getArea() << endl;
     cout << "Perimeter: " << Tri.computePerimeter() << endl;
  }
  catch (exception& ex)
  {
    cout << "Exception occurred!" << endl;
    cout << "Exception ---> ", ex.what();
  }
  return 0;
}