public class removing_duplicates {
    public static void print_list(int[] arr) {
        for (int i = 0; i<arr.length; i++){
            System.out.print(arr[i]);
            System.out.print(" ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int[] list = {1,1,2,2,2,3,3,4,4};
        int index = 1;
        for (int i = 1; i < list.length; i++){
            if (list[i] != list[i-1]){
                list[index] = list[i];
                index++;
            }
        }
        int[] new_list = new int[index];
        System.arraycopy(list, 0, new_list, 0, index);
        print_list(new_list);
    }
}
