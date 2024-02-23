#ifndef ANIMALE_H
#define ANIMALE_H
#include <string>

using namespace std;

class Animale
{
    public:
        //Aniamle();
        Animale(string nome,int eta, int numero_zampe);
        Animale(int eta, int numero_zampe, float peso, string nome);
        //int getEta();
        //int getNumero_zampe();
        //float getPeso();
        string getNome();
    /*
        Bicycle();
        Bicycle(int c, int g, int s);
        void changeCadence(int c);
        void changeGear(int g);
        void speedUp(int inc);
        void applyBrakes(int dec);
        void printStates();
        void setSpeed(int s);
        int getSpeed();
        void doubleSpeed();
    */

    private:
        int eta;
        int numero_zampe;
        float peso;
        string nome;
        bool maggiorenne;
};
#endif