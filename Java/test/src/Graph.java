import java.util.HashMap;
import java.util.HashSet;
import java.util.Deque;
import java.util.LinkedList;

class Graph {

    HashMap<Integer, HashSet<Integer>> adjlist;

    public Graph() {
        this.adjlist = new HashMap<>();
    }

    public void addEdge(int src, int dst) {
        adjlist.putIfAbsent(src, new HashSet<>());
        adjlist.putIfAbsent(dst, new HashSet<>());
        adjlist.get(src).add(dst);
    }

    public boolean removeEdge(int src, int dst) {
        if (!adjlist.containsKey(src) || !adjlist.get(src).contains(dst)) {
            return false;
        }

        adjlist.get(src).remove(dst);
        return true;
    }

    public boolean hasPath(int src, int dst) {
        return hashPathDFS(src, dst, new HashSet<>());
    }

    private boolean hashPathBFS(int src, int dst) {
        HashSet<Integer> visit = new HashSet<>();
        Deque<Integer> que = new LinkedList<>();

        que.add(src);

        while (!que.isEmpty()) {
            int curr = que.poll();
            if (curr == dst) {
                return true;
            }

            visit.add(curr);
            for (int neighbor : adjlist.getOrDefault(curr, new HashSet<>())) {
                if (!visit.contains(neighbor)) {
                    visit.add(neighbor);
                    que.add(neighbor);
                }
            }
        }
        return false;
    }

    private boolean hashPathDFS(int src, int dst, HashSet<Integer> visit) {
        if (src == dst) {
            return true;
        }

        visit.add(src);
        for (int neighbor : adjlist.getOrDefault(src, new HashSet<>())) {
            if (!visit.contains(neighbor)) {
                if (hashPathDFS(neighbor, dst, visit)) {
                    return true;
                }
            }
        }
        return false;
    }
}