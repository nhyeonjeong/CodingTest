#팩토리얼을 재귀로 (DFS)
def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)
print('재귀적으로 표현 :', factorial_recursive(5))
