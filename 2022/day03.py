
score = 0

print(ord("A"))
print(ord("a"))

with open("input03.txt", "r") as file :
    lines = file.readlines()
    count = 1
    first = ""
    middle = []
    for line in lines :
        line = line.strip("\n")
        match count:
            case 1:
                first = line
                count = 2
            case 2 :
                for carac in first :
                    if carac in line :
                        middle.append(carac)
                        count = 3
            case 3 :
                for carac in middle :
                    if carac in line :
                        if ord(carac) >= 97 :
                            print(carac, (ord(carac) - 96))
                            score += (ord(carac) - 96)
                        else :
                            print(carac, (ord(carac) - 38))
                            score += (ord(carac) - 38)
                        count = 1
                        first = ""
                        middle = []
                        break

print(score)
