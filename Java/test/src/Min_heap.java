import java.util.ArrayList;
import java.util.List;

class Min_Heap {
    private List<Integer> min_heap;
    
    public Min_Heap() {
        this.min_heap = new ArrayList<>();
        min_heap.add(0);
    }

    public void push(int val) {
        min_heap.add(val);
        if (min_heap.size() == 2) {
            return;
        }

        int index = min_heap.size() - 1;
        int parent = index / 2;

        while (index > 1 && min_heap.get(index) < min_heap.get(parent)) {
            int temp = min_heap.get(parent);
            min_heap.set(index, min_heap.get(parent));
            min_heap.set(parent, temp);
            index = parent;
            parent = index / 2;
        }
    }

    public int pop() {
        if (min_heap.size() <= 1) {
            return -1;
        } else if (min_heap.size() == 2) {
            return min_heap.remove(1);
        }

        int index = 1;
        int child = index * 2;
        int root = min_heap.get(1);
        min_heap.set(1, min_heap.remove(min_heap.size() - 1));

        if (min_heap.size() > 2) {
            while (index < min_heap.size()) {
                if (child + 1 < min_heap.size() && min_heap.get(child) > min_heap.get(child + 1)) {
                    child++;
                }
                if (min_heap.get(index) <= min_heap.get(child)) {
                    break;
                }

                int temp = min_heap.get(index);
                min_heap.set(index, min_heap.get(child));
                min_heap.set(child, temp);
            }
        }
        return root;
    }

    public int top() {
        return min_heap.size() > 1 ? min_heap.get(1) : -1;
    }

    public void heapify(List<Integer> nums) {
        this.min_heap = new ArrayList<>();
        min_heap.add(0);
        min_heap.addAll(nums);
        int index = min_heap.size() / 2;
        while (index >= 1) {
            int child = index * 2;
            while (child < min_heap.size()) {
                if (child + 1 < min_heap.size() && min_heap.get(child) > min_heap.get(child + 1)) {
                    child++;
                }
                if (min_heap.get(index) <= min_heap.get(child)) {
                    break;
                }

                int temp = min_heap.get(child);
                min_heap.set(child, min_heap.get(index));
                min_heap.set(index, temp);
            }
            index--;
        }
    }

    public void printh() {
        System.out.println(min_heap);
    }
}