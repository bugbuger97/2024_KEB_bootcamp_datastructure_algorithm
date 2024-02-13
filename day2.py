# Stack : First In Last Out
# Queue : First In First Out

# Linear Queue(데이터가 적을 때, 사용)
# enQueue : rear가 증가
# deQueue : front가 증가

# 원형 큐(데이터가 많을 때, 사용)
# 원형 큐가 가득 찼을 때 조건 : (rear값 + 1) % 큐의 SIZE == front값
# enQueue : rear = (rear + 1) % 큐의 SIZE
# deQueue : front = (front + 1) % SIZE

def check_bracket(expr: str) -> bool:
    """
    check bracket in expression.
    :param expr: str
    :return: bool
    """
    stack = list()
    table = {')': '(', ']': '[', '}': '{', '>': '<'}
    for char in expr:
        # if char not in table:
        if char in table.values():  # "([{<"
            stack.append(char)
        elif char in table.keys():  # ")]}>"
            if not stack or table[char] != stack.pop():
                return False
    return len(stack) == 0


if __name__ == "__main__":
    expression = input("Input expression : ")
    print(check_bracket(expression))