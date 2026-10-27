#include<iostream>
#include<cmath>

int main(){
    using std::cout;
    //* A^2 + B^2 = C^2

    int a,b,hy;

    cout << "input a \n";
    std::cin >> a;
    cout << "input b \n";
    std::cin >> b;

    int asq = pow(a,2);
    int bsq = pow(b,2);

    hy = pow(asq+bsq,0.5);
    int hy2 = pow(pow(a,2) + pow(b,2),0.5);
    
    cout << "hy is " << hy << "\n";
    cout << "hy2 is " << hy2 << "\n" ; 


}