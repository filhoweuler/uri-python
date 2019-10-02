
n = int(input())

cast = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for i in range(0,n):
    s = input()
    ans = 0
    for c in s:
        ans += cast[int(c)]
    print("{} leds".format(ans))

    
