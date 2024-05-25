import java.util.List;
import java.util.ArrayList;

class TreeNode {
    int key;
    int val;
    TreeNode left;
    TreeNode right;

    public TreeNode (int key, int val) {
        this.key = key;
        this.val = val;
    }
}

class TreeMap {
    TreeNode root;

    public TreeMap() {
        this.root = null;
    }

    public void insert(int key, int val) {
        TreeNode new_node = new TreeNode(key, val);
        if (root == null) {
            root = new_node;
            return;
        }
        TreeNode curr = root;
        while (true) {
            if (curr.key > key) {
                if (curr.left == null) {
                    curr.left = new_node;
                    return;
                }
                curr = curr.left;
            } else if (curr.key < key) {
                if (curr.right == null) {
                    curr.right = new_node;
                    return;
                }
                curr = curr.right;
            } else {
                curr.val = val;
                return;
            }
        }
    }

    public int get(int key) {
        TreeNode curr = root;
        while (curr != null) {
            if (curr.key < key) {
                curr = curr.left;
            } else if (curr.key > key) {
                curr = curr.right;
            } else {
                return curr.val;
            }
        } 
        return -1;
    }

    public int getMin() {
        TreeNode curr = mini(root);
        return (curr != null) ? curr.val : -1;
    }

    private TreeNode mini (TreeNode curr) {
        while (curr != null && curr.left != null) {
            curr = curr.left;
        }
        return curr;
    }

    public int getMax() {
        TreeNode curr = root;
        while (curr != null && curr.right != null) {
            curr = curr.right;
        }
        return (curr != null) ? curr.val : -1;
    }

    public void remove(int key) {
       root = remover(root, key);
    }

    private TreeNode remover(TreeNode curr, int key) {
        if (curr == null) {
            return null;
        }

        if (curr.key < key) {
            curr.right = remover(curr.right, key);
        } else if (curr.key > key) {
            curr.left = remover(curr.left, key);
        } else {
            if (curr.left == null) {
                return curr.right;
            } else if (curr.right == null) {
                return curr.left;
            } else {
                TreeNode minimum = mini(curr.right);
                curr.key = minimum.key;
                curr.val = minimum.val;
                curr.right = remover(curr.right, minimum.key);
            }
        }
        return curr;
    }

    public List<Integer> getInorderKeys() {
        List<Integer> res = new ArrayList<>();
        inorder(root, res);
        return res;
    }

    private void inorder(TreeNode root, List<Integer> res) {
        if (root != null) {
            inorder (root.left, res);
            res.add(root.key);
            inorder (root.right, res);
        }
    }
}
