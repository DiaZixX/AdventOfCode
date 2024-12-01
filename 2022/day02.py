
score = 0

with open("input02.txt", "r") as file :
    lines = file.readlines()
    for line in lines :
        line = line.strip('\n')
        split = line.split(" ")
        match split[0] :
            case 'A' :
                match split[1] :
                    case 'X' :
                        score += 3 #4
                    case 'Y' :
                        score += 4 #8
                    case 'Z' :
                        score += 8 #3
            case 'B' :
                match split[1] :
                    case 'X' :
                        score += 1 #1
                    case 'Y' :
                        score += 5 #5
                    case 'Z' :
                        score += 9 #9
            case 'C' :
                match split[1] :
                    case 'X' :
                        score += 2 #7
                    case 'Y' :
                        score += 6 #2
                    case 'Z' :
                        score += 7 #6

print(score)
