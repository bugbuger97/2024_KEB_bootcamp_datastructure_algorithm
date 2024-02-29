# recursion memoization
'''
DP 동적 계획법 알고리즘의 핵심.
중복 계산을 제거해서 프로그램의 실행 속도를 빠르게 함. -> 프로그램의 성능 향상

DP란 Dynamic Programming으로
큰 프로그램의 성능을 향상 시키기 위해 작은 부분의 문제를 해결하는 알고리즘 설계 기법임.
1, Optimal Substructure
2, Overlapping Subproblems

- Memoization : 재귀적인 방식으로 작은 부분 문제들을 해결하면서 그 결과를 저장해두고 필요할 때마다 활용하는 방법임.
- Bottom-Up 방식 : 반복문을 이용하여 작은 부분 문제부터 시작하여 순차적으로 큰 문제까지 해결하는 방식임.
'''
def fibo_memoization(number: int) -> int:
    """
    fibonacci function by recursion with memoization.
    :param number: integer number
    :return: integer number
    """
    global memo
    if number >= len(memo):
        memo.append(fibo_memoization(number-1)+fibo_memoization(number-2))
    return memo[number]

memo = [0,1]
if __name__ == "__main__":
    print(fibo_memoization(10))
    print(memo)