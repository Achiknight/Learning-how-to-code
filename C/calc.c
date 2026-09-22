#include <stdio.h>

int main() {
    int op;
    float a,b,res;
    int check = 1;
    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &op);

    printf("Enter two operands: ");
    scanf("%f %f", &a, &b);
    switch (op) {
        case '+':
            res = a + b;
            break;
        case '-':
            res = a - b;
            break;
        case '*':
            res = a * b;
            break;
        case '/':
            res = a / b;
            break;
        default:
            printf("Error! Incorrect Operator Value\n");
            check = 0;
    }
    if (check){
        printf("The operation is %0.2f",res);
    }
    
    return 0;
}