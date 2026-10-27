#include<iostream>
#include<time.h>
int main(){
    using std::cin;
    using std::cout;
    srand(time(0));

    int guess , tries = 0;
    int rng = (rand() % 100)+ 1;
    int found = 0;
    while (!found){
        cout << "Guess your number \n";
        cin >> guess;
        if (guess < -1){
            continue;
        }
        if (guess == rng){
            found = 1;
            cout << "you found the random number in " << tries << " tries" << "\n";
        }
        else if (guess > rng){
            cout << "num is lower than " << guess << "\n";
            tries += 1;
        }
        else if (guess < rng){
            cout << "num is higher than " << guess << "\n";
            tries += 1;
        }        
    }
    
    return 0;
}