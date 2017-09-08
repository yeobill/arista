class SumPaths {
    public static void main(String[] args) {
      testSanity();
      // Write some more test cases
    }

    private static void testSanity() {
      Node root = new Node(1);

      int res = root.sumPaths();
      int expected = 1;

      if (res == expected) {
        System.out.println("Test one passed!");
      } else {
        System.out.println("Test one failed; expected " + expected + " but got " + res + " instead.");
      }
    }
}
