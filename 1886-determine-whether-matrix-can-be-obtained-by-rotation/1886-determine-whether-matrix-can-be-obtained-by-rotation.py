class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        counter = 1
        while counter <= 4:
            if mat == target:
                return True
            for i in range(len(mat)):
                for j in range(i, len(mat)):
                    temp = mat[i][j]
                    mat[i][j] = mat[j][i]
                    mat[j][i] = temp
                mat[i] = mat[i][::-1]
    
            counter += 1
        return False
        
            
        