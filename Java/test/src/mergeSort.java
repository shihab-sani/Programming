public class mergeSort {

    public static void merge(int[] arr, int left, int mid, int right) {
        int length_1 = mid - left + 1;
        int length_2 = right - mid;

        int[] arr_1 = new int[length_1];
        int[] arr_2 = new int[length_2];

        for (int i = 0; i < length_1; i++) {
            arr_1[i] = arr[i + left];
        }
        for (int j = 0; j < length_2; j++) {
            arr_2[j] = arr[mid + 1 + j];
        }

        int i = 0;
        int j = 0;
        int k = left;

        while (i < length_1 && j < length_2) {
            if (arr_1[i] <= arr_2[j]) {
                arr[k] = arr_1[i];
                i++;
            } else {
                arr[k] = arr_2[j];
                j++;
            }
            k++;
        }

        while ( i < length_1) {
            arr[k] = arr_1[i];
            i++;
            k++;
        }

        while (j < length_2) {
            arr[k] = arr_2[j];
            j++;
            k++;
        }
    }

    public static int[] MergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = (left + right) / 2;
            MergeSort(arr, left, mid);
            MergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
        return arr;
    }

    public static void main(String[] args) {
        int[] arr = {23,43,21,34,1,4,323,23,123,32,21};

        MergeSort(arr, 0, arr.length - 1);

        for (int i : arr) {
            System.out.print(i+" < ");
        }
    }
}
