from collections import deque

if __name__ == '__main__':
    que = deque([3, 4, 1, 2, 5])
    que.append(8)
    que.appendleft(9)
    print(que)
    num1 = que.pop()
    num2 = que.popleft()
    print(que)
    print(num1)
    print(num2)
