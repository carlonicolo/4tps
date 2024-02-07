#include <iostream>
#include <vector>
using namespace std;

void simpleMinMaxFor(int min, int max){
    cout << "Inside simpleMinMaxFor(min,max)" << endl;
    for (int i = min; i <= max; i++)
    {
        // cout << i << endl;
        cout << i << " ";
    }
}


void simpleWhileMinMax(int min, int max){
    cout << "Inside simpleWhileMinMax(int min, int max)" << endl;
    while (min <= max)
    {
        cout << min << " ";
        min++;
    }
}

void pariDispari(int min, int max){
    cout << "Inside pariDispari(int min, int max)" << endl;
    for (int i = min; i <= max; i++)
    {
        if (i % 2 == 0)
        {
            cout << "Il numero " << i << " e' pari." << endl;
        }
        else
        {
            cout << "Il numero " << i << " e' dispari." << endl;
        }
    }
}


void simpleVectorloop(int min, int max){
    cout << "Inside simpleVectorloop(int min, int max)" << endl;
    vector<int> v = {10, 45, 21, 88, 109};
    for (int i = 0; i < v.size(); i++)
    {
        cout << "Elemento " << i << " = " << v[i] << endl;
    }
}

int main()
{

    // Task 1 FOR stampa i numeri da 1 a 100
    int min = 1;
    int max = 100;

    // Task 1 FOR stampa i numeri da 1 a 100
    cout << "########## Task 1 #################\n";
    /* for (int i = min; i <= max; i++)
    {
        // cout << i << endl;
        cout << i << " ";
    } */
    simpleMinMaxFor(min,max);
    cout << "\n###########################" << endl;
    cout << "\n";

    // Task 2 WHILE - stampa i valori da min a max
    cout << "\n########## Task 2 #################\n";
    /*
    while (min <= max)
    {
        cout << min << " ";
        min++;
    }
    */
    simpleWhileMinMax(min, max);
    cout << "\n###########################\n"
         << endl;
    cout << "\n";
    

    // Task 3 scegli tu se con FOR o WHILE stampa i valori da 1 a 100
    // e se un valore è pari stampi "pari" se è dispari "dispari"
    cout << "\n########## Task 3 #################\n";

    /*
    min = 1;
    max = 100;

    for (int i = min; i <= max; i++)
    {
        if (i % 2 == 0)
        {
            cout << "Il numero " << i << " e' pari." << endl;
        }
        else
        {
            cout << "Il numero " << i << " e' dispari." << endl;
        }
    }
    */
    pariDispari(min, max);
    cout << "\n###########################\n"
         << endl;
    cout << "\n";

    // Task 4 FOR stampa i valori contenuti nell'array e vector {1,2,3,4,5}
    cout << "\n########## Task 4 #################\n";
    /*
    vector<int> v = {10, 45, 21, 88, 109};
    for (int i = 0; i < v.size(); i++)
    {
        cout << "Elemento " << i << " = " << v[i] << endl;
    }
    */
    
    simpleVectorloop(min, max);
    cout << "\n###########################\n"
         << endl;
    cout << "\n";
}
