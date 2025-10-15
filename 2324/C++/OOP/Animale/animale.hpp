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
        
        // get
        int getEta();
        int getNumeroZampe();
        float getPeso();
        string getNome();
        
        // set
        void setEta(int eta);
        void setNumeroZampe(int numzampe);
        void setPeso(float peso);
        void setNome(string nome);
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