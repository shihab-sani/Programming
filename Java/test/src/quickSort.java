public class quickSort {

    public static int[] QuickSort(int[] arr, int left, int right) {
        if (left < right) {
            int pivot = arr[right];
            int start = left;

            for (int i = left; i < right; i++) {
                if (arr[i] < pivot) {
                    int temp = arr[start];
                    arr[start] = arr[i];
                    arr[i] = temp;
                    start++;
                }
            }
            arr[right] = arr[start];
            arr[start] = pivot;

            QuickSort(arr, left, start - 1);
            QuickSort(arr, start + 1, right);

            return arr;
        }
        return arr;
    }
    public static void main(String[] args) {
        int[] arr = {23,43,21,34,1,4,323,23,123,32,21};

        QuickSort(arr, 0, arr.length - 1);

        for (int i : arr) {
            System.out.print(i+" < ");
        }
    }
}
