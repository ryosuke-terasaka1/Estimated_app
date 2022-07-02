n = int(input())
max_length = -1
max_start_day = 0
max_end_day = 0

a = [int(input()) for _ in range(n)]
is_start = True
i = 0

while i < n-1:
    if is_start:
        start_day = a[i]
        is_start = False

    if a[i+1] - a[i] > 1:
        is_start = True
        if max_length < a[i] - start_day:
            max_start_day = start_day
            max_end_day = a[i]
            max_length = a[i] - start_day
    
    i += 1

if not (max_start_day or max_end_day):
    max_start_day, max_end_day = a[0], a[0]

print(max_start_day, max_end_day)
