#include "animale.hpp"
#include <iostream>
#include <string>

using namespace std;

/*
Animale::Animale()
{
    eta = 0;
    numero_zampe = 0;
    peso = 0;
    nome = "";
    maggiorenne = false;
}
*/

Animale::Animale(string a_nome, int a_eta, int a_numero_zampe)
{
    nome = a_nome;
    eta = a_eta;
    numero_zampe = a_numero_zampe;
}

Animale::Animale(int a_eta, int a_numero_zampe, float a_peso, string a_nome)
{
    eta = a_eta;
    numero_zampe = a_numero_zampe;
    peso = a_peso;
    nome = a_nome;

    if(eta >= 18){
      maggiorenne = true;
    }
    else{
      maggiorenne = false;
    }
}


string Animale::getNome()
{
    return nome;
}