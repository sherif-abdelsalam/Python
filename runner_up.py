

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m1 = max(arr)
    m2 = -9999999999

    print(arr)

    for score in arr:
        if score != m1 and score > m2:
            m2 = score
    
    print (m2)
