#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

void pariDispari(int min, int max)
{
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

// Function to check if a
// given number is prime
bool isPrime(int n)
{
    // Since 0 and 1 is not
    // prime return false.
    if (n == 1 || n == 0)
        return false;

    // Run a loop from 2 to n-1
    for (int i = 2; i < n; i++)
    {
        // if the number is divisible by i,
        // then n is not a prime number.
        if (n % i == 0)
            return false;
    }
    // Otherwise n is a prime number.
    return true;
}

int main()
{

    // Task 1 FOR stampa i numeri da 1 a 100
    int min = 1;
    int max = 20;

    // Task 1 FOR stampa i numeri da 1 a 100
    cout << "########## Task 1 #################\n";
    for (int i = min; i <= max; i++)
    {
        // cout << i << endl;
        cout << i << " ";
    }

    // Task 2 scegli tu se con FOR o WHILE stampa i valori da 1 a 100
    // e se un valore è pari stampi "pari" se è dispari "dispari"
    cout << "\n########## Task 2 #################\n";

    pariDispari(min, max);
    cout << "\n###########################\n"
         << endl;
    cout << "\n";

    // Task 3 stampa i primi 5 numeri primi
    int N = 100;
    int counter = 0;

    // Check for every number from 1 to N
    for (int i = 1; i <= N; i++)
    {
        // Check if current number is prime
        if (isPrime(i))
        {
            counter++;
            cout << i << " ";
        }
    }

    cout << "\n" << counter << " numeri primi" << endl;
}
