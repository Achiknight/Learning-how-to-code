#include<stdio.h>
#include<time.h>
#include<stdlib.h>

int main(){
    srand(time(0));
    int rng = (rand() % 100) + 1;
    int guess = -1;
    int attempt = 1;
    while (guess != rng)
    {
        printf("Enter your guess\n");
        scanf("%d",&guess);
        if (guess == rng){
            printf("You guessed the correct number (%d) in %d attempts",guess,attempt);
            break;
        }
        else if (guess == -67)
        {
            printf("CHEAT MODE THE RANDOM NUMBER IS {%d}\n",rng);
        }
        
        else{
            attempt++;
            if (guess > rng){
                printf("The number is lower than the guessed number (%d)\n",guess);
            }
            else if (guess < rng){
                printf("The number is higher than the guessed number (%d)\n",guess);
            }
        }
    }
    

return 1;

}