class Solution:
    def mySqrt(self, x: int) -> int:
        # i use newton's method for search root of number
        if x == 0:
            return x
        
        xn = x
        epsilon = 0.001

        while True:
            xn_next = (xn + (x/xn)) / 2

            if abs(xn_next - xn) < epsilon:
                break
            xn = xn_next
        return int(xn_next)
            