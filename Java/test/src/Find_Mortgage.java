import java.util.Scanner;
import java.lang.Math;
import java.text.NumberFormat;

public class Find_Mortgage {
    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        System.out.print("Principal: ");
        long p = n.nextLong();

        Scanner m = new Scanner(System.in);
        System.out.print("Annual Interest Rate: ");
        Float a = m.nextFloat();

        Scanner l = new Scanner(System.in);
        System.out.print("Period (Years): ");
        int y = l.nextInt();

        Float rate = (a/100)/12; // percent = 100
        long month = y*12;   // 12 month a year
        double M = (p*rate*(Math.pow(1+rate, month)))/((Math.pow(1+rate, month))-1); // formula
        
        NumberFormat mortgage = NumberFormat.getCurrencyInstance();
        String result = mortgage.format(M);
        System.out.println("Mortgage: "+ result);

    }
}
