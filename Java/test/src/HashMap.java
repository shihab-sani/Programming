class Pair {
    int key;
    int val;
    Pair next;

    public Pair (int key, int val) {
        this.key = key;
        this.val = val;
        this.next = null;
    }
}

class HashTable {
    private int cap;
    private Pair[] map;
    private int size;

    public HashTable(int capacity) {
        this.cap = capacity;
        this.map = new Pair[this.cap];
        this.size = 0;
    }

    private int hash(int key) {
        return key % this.cap;
    }

    public void insert(int key, int value) {
        int index = this.hash(key);
        Pair node = this.map[index];

        if (node == null) {
            this.map[index] = new Pair(key, value);
            this.size++;
        } else {
            Pair prev = null;
            while (node!= null) {
                if (node.key == key) {
                    node.val = value;
                    return;
                }
                prev = node;
                node = node.next;
            }
            prev.next = new Pair(key, value);
            this.size++;
        }

        if ((double) this.size / this.cap >= 0.5) {
            this.resize();
        }
    }

    public int get(int key) {
        int index = this.hash(key);
        Pair node = this.map[index];

        while (node != null) {
            if (node.key == key) {
                return node.val;
            }
            node = node.next;
        }
        return -1;
    }

    public boolean remove(int key) {
        if (this.get(key) == -1) {
            return false;
        }

        int index = hash(key);
        Pair node = this.map[index];
        Pair prev = null;

        while (node != null) {
            if (node.key == key) {
                if (prev != null) {
                    prev.next = node.next;
                } else {
                    this.map[index] = node.next;
                }
                this.size--;
                return true;
            }
            prev = node;
            node = node.next;
        }
        return false;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.cap;
    }

    public void resize() {
        this.cap *= 2;
        Pair[] new_map = new Pair[this.cap];

        for (Pair node: this.map) {
            while (node != null) {
                int index = node.key % this.cap;
                if (new_map[index] == null) {
                    new_map[index] = new Pair(node.key, node.val);
                } else {
                    Pair new_node = new_map[index];
                    while (new_node.next != null) {
                        new_node = new_node.next;
                    }
                    new_node.next = new Pair(node.key, node.val);
                }
                node = node.next;
            }
        }
        this.map = new_map;
    }
}