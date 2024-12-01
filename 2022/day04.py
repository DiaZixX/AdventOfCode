
score = 0

with open("input04.txt", "r") as file :
    lines = file.readlines()
    for line in lines :
        line = line.strip('\n')
        print(line)
        left = line.split(',')[0]
        right = line.split(',')[1]
        ll = int(left.split('-')[0], 10)
        lr = int(left.split('-')[1], 10)
        rl = int(right.split('-')[0], 10)
        rr = int(right.split('-')[1], 10)

        e = max(ll, rl)
        f = min(lr, rr)

        #if (ll <= rl and rr <= lr) or (rl <= ll and lr <= rr) :
        #    score += 1
        if e <= f :
            score += 1

print(score)

