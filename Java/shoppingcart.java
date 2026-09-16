package Java;
import java.util.Scanner;

public class shoppingcart {
    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        int amount ;
        float price;
        System.out.print("Enter the item: ");
        String item = sc.nextLine();

        System.out.print("Enter the price$: ");
        price = sc.nextFloat();

        System.out.print("enter the amount: ");
        amount = sc.nextInt();

        float total = price*amount;

        System.out.println("The total is of your "+amount+" "+item+" is "+total+"$");





        sc.close();
    }
}