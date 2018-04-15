#include <iostream>

using namespace std;

void epsilonSimpleM1(float D){
    while(1 != 1 + D){
        cout << D << endl;
        D = D / 2;
    }
}

void epsilonDobleM1(double D){
    while(1 != 1 + D){
        cout << D << endl;
        D = D / 2;
    }
}

void epsilonSimpleM2(float D){
    while(0 != D){
        cout << D << endl;
        D = D / 2;
    }
}

void epsilonDobleM2(double D){
    while(0 != D){
        cout << D << endl;
        D = D / 2;
    }
}

int main(void){
    float F = 0.5;
    double D = 0.5;
    cout << "Método 1 Simple" << endl;
    epsilonSimpleM1(F);
    cout << "Método 1 Doble" << endl;
    epsilonDobleM1(D);
    cout << "Método 2 Simple" << endl;
    epsilonSimpleM2(F);
    cout << "Método 2 Doble" << endl;
    epsilonDobleM2(D);
    return 0;
}