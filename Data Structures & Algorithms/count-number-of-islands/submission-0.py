class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        land = "1"
        water = "0"

        def search(row, col):
            if visited[row][col]:
                return
            visited[row][col] = True
            
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if (k == 0 or l == 0) and not (k == 0 and l == 0):
                        if 0 <= row+k < n and 0 <= col+l < m and not visited[row+k][col+l]:
                            if grid[row+k][col+l] == water:
                                visited[row+k][col+l] = True
                                continue
                            else:
                                search(row+k, col+l)


        ans = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j]:
                    continue
                if grid[i][j] == land:
                    ans += 1
                    search(i, j)

        return ans
                

