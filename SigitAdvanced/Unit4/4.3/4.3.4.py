def get_fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))

print("\n=========================================\n")

ten_fibo_nums = get_fibo()
for i in range(10):
    print(next(ten_fibo_nums))