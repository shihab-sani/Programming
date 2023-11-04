
for i in range(int(input())):
    a = input()
    s = 0
    count = 0
    for j in range(len(a)):
        o = len(a)//6
        v = len(a)-6*o
        if len(a)>6:
            c='Overs'
        else:
            c='Over'
        if a[j] == "W":
            count += 1
        else:
            s += int(a[j])
        if count > 1:
            w = "Wickets"
        else:
            w = "Wicket"
        if s > 1:
            r = "Runs"
        else:
            r = "Run"
    print(f"{o}.{v} {c} {s} {r} {count} {w}.")
            