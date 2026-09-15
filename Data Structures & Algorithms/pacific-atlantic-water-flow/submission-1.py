class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def reach(starts):
            seen = set(starts)
            q = deque(starts)
            while q:
                r, c = q.popleft()
                for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in seen
                            and heights[nr][nc] >= heights[r][c]):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            return seen

        pac = reach([(0, c) for c in range(COLS)] + [(r, 0) for r in range(1, ROWS)])
        atl = reach([(ROWS-1, c) for c in range(COLS)] + [(r, COLS-1) for r in range(ROWS-1)])
        return [[r, c] for r, c in pac & atl]