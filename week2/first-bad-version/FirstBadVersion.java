/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class FirstBadVersion extends VersionControl {
    public int firstBadVersion(int n) {
        for (int i = n; i > 1; i--) {
            if (!isBadVersion(i)) {
                return i+1;
            }
        }
        return 1;
    }
}