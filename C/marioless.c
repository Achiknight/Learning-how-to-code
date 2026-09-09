#include <stdio.h>

int main() {
    int lenght;-
    scanf("%d",&lenght);

    for (int i = 0; i<lenght;i++){
        for (int j = 1; j < lenght-i;j++){
            printf(" ");
        }
        for (int k = 0; k<=i;k++){
            printf("#");
        }
        printf("\n");
    }
    return 0;
}