#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        print("{}".format(str(i) + str(j)), end="")
        if int(str(i) + str(j)) < 89:
            print(", ", end="")
print("")
