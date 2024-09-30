#include <iostream>
#include <string>
using namespace std;

int main()
{
    string magic_word = "hello";
    string try_word = ""; 
    int numero_tentativi = 0;

    while(numero_tentativi < 3){
        cout << "Inserisci la parola magica" << endl;
        cin >> try_word;
        if(magic_word == try_word){
            cout << "Hai vinto in " << (numero_tentativi + 1) << " tentativi" << endl;
            break;
        }
        else{
            cout << "Ritenta sarai più fortunato!!!" << endl;
            numero_tentativi++;
        }

    }

    if(numero_tentativi < 3){
        cout << "Hai superato il prmo livello" << endl;
        cout << "Secondo livello" << endl;
    }
    else{
        cout << "Hai perso!!!" << endl;
    }

    return 0;
}
