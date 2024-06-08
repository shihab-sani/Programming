import java.util.ArrayDeque;
import java.util.Deque;

class BFS {
    public int shortestPath(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int length = 0;
        int[][] visit = new int[4][4];
        Deque<int[]> que = new ArrayDeque<>();

        que.add(new int[2]);
        visit[0][0] = 1;

        while (!que.isEmpty()) {
            int qlength = que.size();
            for (int i = 0; i < qlength; i++) {
                int[] pair = que.poll();
                int row = pair[0];
                int col = pair[1];

                if (row == (rows - 1) && col == (cols - 1)) {
                    return length;
                }

                int[][] direction = {{row + 1, col}, {row - 1, col}, {row, col + 1}, {row, col - 1}};
                for (int j = 0; j < 4; j++) {
                    int new_row = direction[j][0];
                    int new_col = direction[j][1];
                    if (Math.min(new_row, new_col) < 0 || new_row == rows || new_col == cols || visit[new_row][new_col] == 1 || grid[new_row][new_col] == 1) {
                        continue;
                    } 

                    que.add(direction[j]);
                    visit[new_row][new_col] = 1;
                }
            }
            length++;
        }
        return -1;
    }
}