public class MergeList {

    public static int[] merge(int[] arr_1, int[] arr_2) {

        if (arr_2 == null) {
            return arr_1;
        }

        int[] arr = new int[(arr_1.length + arr_2.length)];
        int i = 0;
        int j = 0;
        int k = 0;
    
        while (i < arr_1.length && j < arr_2.length) {
            if (arr_1[i] <= arr_2[j]) {
                arr[k] = arr_1[i];
                i++;
            } else {
                arr[k] = arr_2[j];
                j++;
            }
            k++;
        }

        while (i < arr_1.length) {
            arr[k] = arr_1[i];
            i++;
            k++;
        }
    
        while (j < arr_2.length) {
            arr[k] = arr_2[j];
            j++;
            k++;
        }
        return arr;
    }

    public static int[] mergelist(int[][] array) {

        if (array == null || array.length == 0) {
            return null;
        }

        int[] arr_1;
        int[] arr_2; 

        while (array.length > 1) {
            int[][] result = new int[(array.length + 1) / 2][];
            for (int i = 0; i < array.length; i += 2) {
                arr_1 = array[i];
                if (i+1 < array.length) {
                    arr_2 = array[i + 1];
                } else {
                    arr_2 = null;
                }
                result[i/2] = merge(arr_1, arr_2);
            }
            array = result;
        }
        return array[0];
    }

    public static void main(String[] args) {
        int[][] arr = {{1,3,5},{2,4,6},{7,9},{8,10}};

        int[] res = mergelist(arr);

        for (int i : res) {
            System.out.print(i+" ,");
        }
    }
}