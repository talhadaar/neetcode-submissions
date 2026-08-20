class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # start BFS, since we have to colore adjacent pixels only?
        # mark visited and =2 if not

        orig = image[sr][sc]
        if orig == color:
            return image
        nei = [(-1,0),(1,0),(0,-1),(0,1)]

        ROWS = len(image)
        COLS = len(image[0])

        q = deque()
        q.append((sr,sc))
        image[sr][sc] = color

        while q:
            r0,c0 = q.popleft()
            for rd,cd in nei:
                rn,cn = r0+rd, c0+cd
                if 0 <= rn < ROWS and 0 <= cn < COLS and image[rn][cn]==orig:
                    image[rn][cn] = color
                    q.append((rn,cn))

        return image