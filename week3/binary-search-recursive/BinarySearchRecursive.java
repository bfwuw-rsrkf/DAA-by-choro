class BinarySearchRecursive {
    public static void main(String[] args){
        int[] arr1 = {7, 11, 13, 18, 20};
        int[] arr2 = {3, 5, 14, 17, 18};
        int[] arr3 = {7, 10, 12, 15, 20};

        System.out.println(binarySearchRecursive(arr1, 0, arr1.length-1, 7));
        System.out.println(binarySearchRecursive(arr2, 0, arr2.length-1, 7));
        System.out.println(binarySearchRecursive(arr3, 0, arr3.length-1, 7));
    }

    public static int binarySearchRecursive(int[] a, int low, int high, int target) {
        if (high < low) {
            return -1;
        }
        int mid = low + (high - low) / 2;

        if (a[mid] == target) {
            return mid;
        }
        else if (target < a[mid]) {
            return binarySearchRecursive(a, low, mid - 1, target);
        }
        else {
            return binarySearchRecursive(a, mid + 1, high, target);
        }
    }
}