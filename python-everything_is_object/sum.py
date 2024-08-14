buzz = 1

def sum():
    global buzz
    buzz += 1

buzz = 3
sum()

print(buzz)