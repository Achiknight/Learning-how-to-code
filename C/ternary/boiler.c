#include <stdio.h>

// char,int isbigger(int a,int b,int c){
//     char big;
//     int temp;




//     return
// }


int main() {
    int a = 1,b = 5,c = 3;
    int temp;

    temp = a>b?a>c?a:c:b>c?b:c;
    printf("temp is %d",temp);

    return 0;

}