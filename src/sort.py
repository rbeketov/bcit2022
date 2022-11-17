data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    sort_lambda = lambda x : sorted(x, reverse=True)
    result = sorted(data, reverse=True)
    print(result)
    print(sort_lambda(data))