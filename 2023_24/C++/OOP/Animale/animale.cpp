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

int Animale::getEta()
{
    return eta;
}

int Animale::getNumeroZampe()
{
    return numero_zampe;
}

float Animale::getPeso()
{
    return peso;
}


void Animale::setEta(int s_eta){ eta = s_eta; }
void Animale::setNumeroZampe(int s_numzampe){ numero_zampe = s_numzampe; }
void Animale::setPeso(float s_peso){ peso = s_peso; }
void Animale::setNome(string s_nome){ nome = s_nome; }