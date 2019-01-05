from random import randint
# input the level
level = input("Enter the level you want (Easy, Medium or Difficult): ").lower()

# generate map due to the level
if level == "easy":
    n = 8
    mines_count = 10
if level == "medium":
    n = 16
    mines_count = 40
if level == "difficult":
    n = 24
    mines_count = 99

map = []

for i in range(n):
    map.append([])
for i in range(n):
    for j in range(n):
        map[i].append(j)

for i in range(n):
    for j in range(n):
        map[i][j] = 0

# generate mines in random
for m in range(mines_count):
    i = randint(0, n-1)
    j = randint(0,n-1)
    map[i][j] = 9

# render basic map
for i in range(n):
    for j in range(n):
        if map[i][j] != 9:
            if i == 0 and j == 0 :
                if map[i+1][j] ==9:
                    map[i][j] +=1
                if map [i][j+1] == 9:
                    map[i][j] +=1
                if map [i+1][j+1] == 9:
                    map[i][j] +=1
            elif i == 0 and j == n-1 :
                if map[i+1][j] ==9:
                    map[i][j] +=1
                if map [i][j-1] == 9:
                    map[i][j] +=1
                if map [i-1][j-1] == 9:
                    map[i][j] +=1
            elif i == n-1 and j == 0 :
                if map[i-1][j] ==9:
                    map[i][j] +=1
                if map [i][j+1] == 9:
                    map[i][j] +=1
                if map [i-1][j+1] == 9:
                    map[i][j] +=1
            elif i == n-1 and j == n-1 :
                if map[i-1][j] ==9:
                    map[i][j] +=1
                if map [i][j-1] == 9:
                    map[i][j] +=1
                if map [i-1][j-1] == 9:
                    map[i][j] +=1
            
            elif (i == 0 and j != 0) and (i==0 and j != n-1):
                if map[i][j-1] ==9:
                    map[i][j] +=1
                if map[i][j+1] ==9:
                    map[i][j] +=1
                if map[i+1][j-1] ==9:
                    map[i][j] +=1
                if map[i+1][j+1] ==9:
                    map[i][j] +=1
                if map[i+1][j] ==9:
                    map[i][j] +=1

            elif (i == n-1 and j != 0) and (i==n-1 and j != n-1):
                if map[i][j-1] ==9:
                    map[i][j] +=1
                if map[i][j+1] ==9:
                    map[i][j] +=1
                if map[i-1][j+1] ==9:
                    map[i][j] +=1
                if map[i-1][j-1] ==9:
                    map[i][j] +=1
                if map[i-1][j] ==9:
                    map[i][j] +=1

            elif (i != n-1 and j == 0) and (i!=0 and j == 0):
                if map[i+1][j] ==9:
                    map[i][j] +=1
                if map[i-1][j] ==9:
                    map[i][j] +=1
                if map[i+1][j-1] ==9:
                    map[i][j] +=1
                if map[i+1][j+1] ==9:
                    map[i][j] +=1
                if map[i][j+1] ==9:
                    map[i][j] +=1

            elif (i != n-1 and j == n-1) and (i!=0 and j == n-1):
                if map[i+1][j] ==9:
                    map[i][j] +=1
                if map[i-1][j] ==9:
                    map[i][j] +=1
                if map[i-1][j-1] ==9:
                    map[i][j] +=1
                if map[i+1][j-1] ==9:
                    map[i][j] +=1
                if map[i][j-1] ==9:
                    map[i][j] +=1

            else :
                if map[i+1][j] ==9:
                    map[i][j] +=1
                if map[i+1][j+1] ==9:
                    map[i][j] += 1
                if map[i+1][j-1] ==9:
                    map[i][j] += 1
                if map[i-1][j] ==9:
                    map[i][j] +=1
                if map[i-1][j+1] ==9:
                    map[i][j] += 1
                if map[i-1][j-1] ==9:
                    map[i][j] += 1
                if map[i][j+1] ==9:
                    map[i][j] += 1
                if map[i][j-1] ==9:
                    map[i][j] += 1

a = " "
def render_map():
    for i in range(n):
        for j in range(n):
            if j != n-1:
                if map[i][j] != 9:
                    print("!"+a, end="")
                if map[i][j] == 9:
                    print("!"+a, end="")
            if j == n-1:
                if map[i][j] != 9:
                    print("!"+a+"!", end="")
                if map[i][j] == 9:
                    print("!"+a+"!", end="")
        print()
                
# test the map
render_map()
for i in range(n):
    print(map[i])

def revealed(x,y):
    for i in range(n):
        for j in range(n):
            if i == x and j == y:
                a = str(map[i][j])
            else:
                a = " "
            if j != n-1 :
                if map[i][j] != 9:
                    print("!"+a, end="")
                if map[i][j] == 9:
                    print("!"+a, end="")
            if j == n-1:
                if map[i][j] != 9:
                    print("!"+a+"!", end="")
                if map[i][j] == 9:
                    print("!"+a+"!", end="")
        print()

loop = True
while loop:
    dx = int(input("input the x_coor "))
    dy = int(input("input the y_coor "))

