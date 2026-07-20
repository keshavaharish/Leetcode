class Solution(object):
    def shiftGrid(self, grid, k):
        m,n=len(grid),len(grid[0])
        while k:
            cur=[[0]*n for _ in range(m)]
            for r in range(m):
                for c in range(n-1):
                    cur[r][c+1]=grid[r][c]
            for r in range(m):
                cur[(r+1)%m][0]=grid[r][n-1]
            grid=cur
            k-=1
        return grid
        