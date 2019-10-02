while True:
    s = input()
    s = s.split(" ")

    a = int(s[0])
    b = int(s[1])

    if a == 0 and b == 0:
        break

    num_st = str(a+b).replace("0", "")

    print(num_st)
