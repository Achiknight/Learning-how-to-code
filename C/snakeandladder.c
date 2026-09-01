#include <stdio.h>
#include<stdlib.h>
#include<time.h>
#include <windows.h>
#include<string.h>

void printarr(char arr[][10][10]){
    SetConsoleOutputCP(CP_UTF8);
    for (int i = 0; i<10;i++){
        for (int j = 0; j<10;j++){
            char *ptr = arr[i][j];
            printf("%s",ptr);

        }
    printf("\n");
    }

}


int main(){
    SetConsoleOutputCP(CP_UTF8);
    srand(time(NULL));
    int player1 = 0;
    int player2 = 0;
    
    printf("__SNAKE AND LADDER___\n");
    printf("□ is a free square\n");
    printf("■ is a danger square\n");
    printf("Player One is " "\033[34m" "■" "\033[0m\n");
    printf("Player Two is " "\033[33m" "■" "\033[0m\n");
    const char *Free = "\033[0m□";
    const char *snake = "\033[31m■";
    char board[10][10][10];

    for (int i = 0; i <10;i++){                     // to make the board
        for (int j = 0; j <10 ; j++){
            if ((i == 0 && j == 0) || (i == 9 && j == 9)){
                strcpy(board[i][j],Free);
                continue;
            }
            int pot = (rand() % 10) + 0;
            if (pot == 1){

                strcpy(board[i][j],snake);
            }
            else{
                strcpy(board[i][j],Free);
            }
        }
    }
    // printarr(board);
    // printf("Bro \n");
    // printf("%s",board[3][4]);

    const char *P1 = "\033[34m■";
    const char *P2 = "\033[33m■";

        while ((player1 < 100) && (player2 < 100)){
            printf("Player 1's turn (press enter)\n");

            while (getchar() != '\n'){}
            int rngp1 = (rand() % 6) + 1;
            printf("You rolled %d\n \n", rngp1);
            player1 += rngp1;
            int p1I = player1/10;
            int p1J = player1%10;
            
            strcpy(board[p1I][p1J],P1);

            printf("Player 2's turn (press enter)\n");

            while (getchar() != '\n'){}
            int rngp2 = (rand() % 6) + 1;
            printf("You rolled %d\n \n", rngp2);
            player2 += rngp2;
            int p2I = player2/10;
            int p2J = player2%10;
            
            strcpy(board[p2I][p2J],P2);

            printarr(board);
        }
        return 0;
}