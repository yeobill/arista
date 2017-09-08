class Node {
  private final int value;
  private Node left = null;
  private Node right = null;

  public Node(int val) {
    this.value = val;
  }

  public Node right() {
    return this.right;
  }

  public Node left() {
    return this.left;
  }

  public void setRight(Node r) {
    this.right = r;
  }

  public void setLeft(Node l) {
    this.left = l;
  }

  public int value() {
    return this.value;
  }

  public int sumPaths() {
    // IMPLEMENT ME
    throw new java.lang.UnsupportedOperationException("Not implemented yet.");
  }
}
