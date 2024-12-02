text = """3   4
4   3
2   5
1   3
3   9
3   3"""

text = text.split("\n")
l1 = []
l2 =[] 
for i in text:
    i = i.split(" ")
   
    l1.append(i[0])
    l2.append(i[-1])
sum = 0
simScore = 0
l1.sort()
l2.sort()
for i in range(len(l1)):
    simScore += int(l1[i])*l2.count(l1[i])
    sum += abs(int(l1[i])-int(l2[i]))
print(sum)
print(simScore)