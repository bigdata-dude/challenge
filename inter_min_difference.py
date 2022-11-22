ls1 = [45,55,64,18,93]
target = 60
newList =[]
for n in ls1:
    newList.append(abs(n-target))
newList.sort()
print(min(newList))
print(newList)

print("Conclud")