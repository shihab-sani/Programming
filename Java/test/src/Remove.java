// Remove k-th value from array

public class Remove {

    public static void print_list(int[] arr) {
        for (int i = 0; i<arr.length; i++){
            System.out.print(arr[i]);
            System.out.print(" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int[] list = {1,2,3,4};
        int k = 1;     // k-th index will be deleted 
        for (int i = k+1; i < list.length; i++){
            list[i-1] = list[i];
        }
        int size = list.length-1;
        int[] new_list = new int[size];
        System.arraycopy(list, 0, new_list, 0, size);
        print_list(new_list);
    }
}