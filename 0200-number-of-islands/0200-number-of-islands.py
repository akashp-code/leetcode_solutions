class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        directions = [
            (-1,0),
            (+1,0),
            (0,-1),
            (0,+1)
        ]      

        def dfs(r,c):
            visited.add((r,c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr,nc) not in visited):

                    dfs(nr, nc)

        island = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and (r,c) not in visited :

                    island += 1

                    dfs(r,c)

        return island


                    
                












                    
                      

                 





    