#!/usr/bin/env python

import hashlib as hl

i = 0

with open("input04.txt", "r") as file:
    key = file.read().strip("\n")
    while True:
        attempt = key + str(i)
        hash = hl.md5(attempt.encode()).hexdigest()
        if hash[:6] == "000000":
            break
        i += 1
    file.close()

print(i)
