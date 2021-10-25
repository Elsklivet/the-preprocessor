
public class Test2 {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        for(int i = 0; i < 4; i++) {
            System.out.println(i);
        }
        if(true) System.out.println("True!");
    }
public class Node { 
    String data;
    Node next;

    public Node(String str) { this.data = str; this.next = null; }
    public Node(String str, Node nex) { this.data = str; this.next = nex; }
}
}
