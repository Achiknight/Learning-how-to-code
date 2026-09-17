package Java;

import java.util.Scanner;

public class if_eleif_else {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter your age: ");
        int age = sc.nextInt();

        if (age <0){
            System.out.println("you are not born yet");
        }
        else if (age >= 65){
            System.out.println("You are senior");
        }

        else if (age >= 18){
            System.out.println("You are adult");
        }
        
        sc.close();
    }
    
}
