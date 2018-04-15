#include <iostream>
#include <stdio.h>
#include <cmath>
#include <math.h>

using namespace std;

double f(double x){
    const double e = std::exp(1.0);
    return pow(e,x) - x - 2;
}

void buscarIncremento(double x0, double delta, int N){
    double fx0 = f(x0);
    if(fx0 == 0){
        cout << "Se encontró 1 raíz en f(x) = " << x0 << endl;
    }else{
        double x1 = x0 + delta;
        int contador = 1;
        double fx1 = f(x1);

        while(((fx0 * fx1) > 0) && (contador < N)){
            x0 = x1;
            fx0 = fx1;
            x1 = x0 + delta;
            fx1 = f(x1);
            contador = contador + 1;
        }
        if(fx1 == 0){
            cout << "Se encontró 1 raíz en f(x) = " << x1 << endl;
        }else if(fx0 * fx1 < 0){
            cout << "Hay 1 raíz entre [" << x0 << ", " << x1 << "]" << endl;
        }else{
            cout << "Fracasó en " << N << " iteraciones" << endl;
        }
    }
}

int main(void){
    double x0;
    double delta;
    int N;
    cout << "Ingrese el X0: ";
    cin >> x0;
    cout << "Ingrese el deltaX: ";
    cin >> delta;
    cout << "Ingrese el N (# de iteraciones): ";
    cin >> N;
    buscarIncremento(x0, delta, N);
    return 0;
}   