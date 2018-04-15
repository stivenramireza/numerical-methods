#include <iostream>
#include <stdio.h>
#include <cmath>
#include <math.h>

using namespace std;

double f(double x){
    const double e = std::exp(1.0);
    return pow(e,x) - x - 1;
}

void buscarIncremento(double Xcero, double DX, int N){
    int cont = 0;
    double Xant = Xcero;
    double Fant = f(Xcero); 
    double Xact;
    double Fact;

    if(Fant == 0){
        cout << "Se encontró 1 raíz en f(x) = " << Xant << endl;
    }else{
        for(int i = 0; i < N; ++i){
            Xact = Xact + DX;
            Fact = f(Xact);
            if(Fact == 0){
                break;
            }else if(Fact*Fant < 0){
                break;
            }else{
                Xant = Xact;
                Fant = Fact;
            }
            cont++;
        }
        if(cont == N){
            cout << "Se encontró 1 raíz en f(x) = " << Xact << endl;
        }
    }
}

int main(void){
    double Xcero;
    double DX;
    int N;
    cout << "Ingrese el X0: ";
    cin >> Xcero;
    cout << "Ingrese el deltaX: ";
    cin >> DX;
    cout << "Ingrese el N (# de iteraciones): ";
    cin >> N;
    buscarIncremento(Xcero, DX, N);
    return 0;
}   