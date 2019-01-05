# x = [1,2,3]
# y = [1,2,3]
# x.append(4)

# print(x)
# print(y)



# { ( { { ) ( ) } } ) }

# ( { { } } ) }
 
# (1 {2  3) 4} 

# R G B R B G R G G

n = input("Nhap: ")
n = n.split(" ")
print(n)
for i in range(0, len(n)):
    for j in range(i+1, len(n)):
        if (n[i] == "(" and n[j]  == ")"):
            print(i, " ", j)
            print(n[i], " - ", n[j])
        if (n[i] == "{" and n[j] == "}"):
            print(i, " ", j)
            print(n[i], " - ", n[j])
        if (n[i] == "[" and n[j] == "]"):
            print(i, " ", j)
            print(n[i], " - ", n[j])

