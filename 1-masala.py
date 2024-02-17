def fibonachchi(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

N = int(input("Fibonacci sonlari nechta chiqishi kerakligini kiriting: "))
for i in fibonachchi(N):
    print(i)
