def plusOne(digits):
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits

if __name__ == "__main__":
    
    digits = list(map(int, input("Enter digits separated by space: ").split()))
    
    result = plusOne(digits)
    
    print("Result:", result)
