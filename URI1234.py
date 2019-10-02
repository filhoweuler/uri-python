while True:
    try:
        s = list(input())
    except EOFError:
        break
    
    upper = True

    for i, caractere in enumerate(s):
        if caractere == ' ':
            continue

        if caractere.isupper() != upper:
            if upper:
                s[i] = s[i].upper()
            else:
                s[i] = s[i].lower()

        upper = not upper


    print("".join(s))
