#include <iostream>
using namespace std;

int main()
{
    int val;

    cout << "Inserisci un valore intero: " << endl;
    cin >> val ;

    cout << "Il valore è: " << val << " " << endl;

    if(val > 10){
        cout << "Il valore è maggiore di 10" << endl;
        for(int i=0; i < 11; i++){
            cout << i << endl;
        }
    }
    else {
        cout << "Il valore è minore di 10" << endl;
        for(int i=10; i >= 0; i--){
            cout << i << endl;
        }
    }

    return 0;
}
