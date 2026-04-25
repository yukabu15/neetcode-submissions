class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        land = 1
        water = 0
        ans = 0

        def search(row, col):
            if visited[row][col]:
                return
            visited[row][col] = True
            
            for dr, dc in directions:
                if 0 <= row+dr < n and 0 <= col+dc < m and not visited[row+dr][col+dc]:
                    if grid[row+dr][col+dc] == water:
                        visited[row+dr][col+dc] = True
                        continue
                    else:
                        self.current += 1
                        search(row+dr, col+dc)


        ans = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    continue
                if grid[i][j] == land:
                    self.current = 1
                    search(i, j)
                    ans = max(ans, self.current)

        return ans