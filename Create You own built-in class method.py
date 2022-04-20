x = int(input("Enter the value of x: "))
n = int(input("enter the value of n: "))

class py_pow:
    def power(self, x, n):
        if x == 0 or x == 1 or n == 1:
            return x
        if x == 1:
            if x % 2 == 0:
                return 1
            else:
                return -1
        if n == 0:
            return 1
        if n < 0:
            return 1/self.power(x,-n)
        val = self.power(x, n//2)
        if n % 2 == 0:
            return val * val
        return val * val * x
        
print("pow(x, n) value is: ", py_pow().power(x, n))