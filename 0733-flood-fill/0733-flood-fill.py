class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows = len(image)
        col = len(image[0])

        original = image[sr][sc]

        if original == color:
            return image

        dirc = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        
        def dfs(r,c):

            image[r][c] = color

            for dr, dc in dirc:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and 0 <= nc < col and image[nr][nc] == original ):
                    
                    dfs(nr,nc)

        dfs(sr, sc)

        return image

