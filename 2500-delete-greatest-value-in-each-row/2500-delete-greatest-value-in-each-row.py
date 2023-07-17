class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        temp = []
        total = 0
        i = len(grid[0])
        while i > 0:
            for j in range(len(grid)):
                maxEl = max(grid[j])
                temp.append(maxEl)
                grid[j].pop(grid[j].index(maxEl))

            total += max(temp)
            temp.clear()
            i -= 1
        
        return total
        