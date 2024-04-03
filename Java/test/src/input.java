import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.Stream;

public class input {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] arr = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        System.out.println(arr[0]);
    }
}

// import java.util.Arrays;
// import java.util.Scanner;

// public class input {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);

//         String input = scanner.nextLine();
//         String[] st = input.split(" ");

//         System.out.println(Arrays.toString(st));
//     }
// }