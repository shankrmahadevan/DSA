// HackerRank Problem link: https://www.hackerrank.com/challenges/tree-top-view/problem

import java.util.*;

class Node {
    Node left;
    Node right;
    int data;

    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class TreeTopView {

    /*
     * 
     * class Node int data; Node left; Node right;
     */
    static class NodeOrder {
        Node node;
        int dir;

        NodeOrder(Node node, int dir) {
            this.node = node;
            this.dir = dir;
        }
    }

    public static void topView(Node root) {
        Deque<Integer> deque = new LinkedList<>();
        Queue<NodeOrder> q = new LinkedList<>();
        deque.add(root.data);
        int left = 0, right = 0;
        if (root.left != null)
            q.add(new NodeOrder(root.left, -1));
        if (root.right != null)
            q.add(new NodeOrder(root.right, 1));
        while (!q.isEmpty()) {
            int n = q.size();
            for (int i = 0; i < n; i++) {
                NodeOrder x = q.remove();
                if (x.dir < left) {
                    deque.push(x.node.data);
                    left--;
                }
                if (x.dir > right) {
                    deque.offer(x.node.data);
                    right++;
                }
                if (x.node.left != null)
                    q.add(new NodeOrder(x.node.left, x.dir - 1));
                if (x.node.right != null)
                    q.add(new NodeOrder(x.node.right, x.dir + 1));
            }
        }
        for (Iterator itr = deque.iterator(); itr.hasNext();) {
            System.out.print(itr.next() + " ");
        }
    }

    public static Node insert(Node root, int data) {
        if (root == null) {
            return new Node(data);
        } else {
            Node cur;
            if (data <= root.data) {
                cur = insert(root.left, data);
                root.left = cur;
            } else {
                cur = insert(root.right, data);
                root.right = cur;
            }
            return root;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        Node root = null;
        while (t-- > 0) {
            int data = scan.nextInt();
            root = insert(root, data);
        }
        scan.close();
        topView(root);
    }
}