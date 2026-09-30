class BinarySearchIterative {
    public static void main(String[] args){
        int[] arr1 = {7, 11, 13, 18, 20};
        int[] arr2 = {3, 5, 14, 17, 18};
        int[] arr3 = {7, 10, 12, 15, 20};

        System.out.println(binarySearchIterative(arr1, 7));
        System.out.println(binarySearchIterative(arr2, 7));
        System.out.println(binarySearchIterative(arr3, 7));
    }

    public static int binarySearchIterative(int[] a, int target) {
        int low = 0;
        int high = a.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (a[mid] == target) {
                return mid;
            }
            else if (target < a[mid]) {
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        return -1;
    }
}