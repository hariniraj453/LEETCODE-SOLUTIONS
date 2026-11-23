class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        orig = image[sr][sc]
        # Already adhe color na return pannidu
        if orig == color:
            return image
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            # Out of bound illa vera color na stop
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != orig:
                return
            
            image[r][c] = color
            
            # 4 direction
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        dfs(sr, sc)
        return image