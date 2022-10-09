list = [2, 3, 4, 5, 6]
summlist = []
for i in range((len(list)+1)//2):
    summlist.append(list[i]*list[len(list)-1-i])
print(summlist)