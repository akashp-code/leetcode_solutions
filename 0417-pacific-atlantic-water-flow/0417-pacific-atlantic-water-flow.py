class Solution:
    def pacificAtlantic(self, heights):

        if not heights:
            return []

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(r, c, ocean):

            ocean.add((r, c))

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in ocean
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, ocean)

        # Pacific: top + left
        for c in range(cols):
            dfs(0, c, pacific)

        for r in range(rows):
            dfs(r, 0, pacific)

        # Atlantic: bottom + right
        for c in range(cols):
            dfs(rows - 1, c, atlantic)

        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        return list(pacific & atlantic)