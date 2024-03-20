import java.util.Scanner;
import java.lang.Math;
import java.text.NumberFormat;

public class Find_Mortgage {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long p;
        while (true){
            System.out.print("Principal ($1K - $1M): ");
            p = scanner.nextLong();
            if (p >= 1000 && p <= 1000000)
                break;
        }
        
        Float a;
        while (true){
            System.out.print("Annual Interest Rate: ");
            a = scanner.nextFloat();
            if (a > 1 && a <= 30)
                break;
            else
                System.out.println("Enter a value greater than 0 and less or equal to 30.");
        }
        
        int y;
        while (true){
            System.out.print("Period (Years): ");
            y = scanner.nextInt();
            if (y > 0 && y <= 30)
                break;
            else
                System.out.println("Enter a value between 1 and 30.");
        } 
        
        Float rate = (a/100)/12; // percent = 100
        long month = y*12;   // 12 month a year
        double M = (p*rate*(Math.pow(1+rate, month)))/((Math.pow(1+rate, month))-1); // formula
        
        NumberFormat mortgage = NumberFormat.getCurrencyInstance();
        String result = mortgage.format(M);
        System.out.println("Mortgage: "+ result);

        scanner.close();
    }
}