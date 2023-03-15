file = open("111.txt")
s = file.read()
s = s.replace('\n', '')
list = s.split(" ")
r = []
for i in list:
    if len(i) >= 7:
        r.append(i)


final = '\n'.join(r)
print(final)
file2 = open("333.txt", "w", encoding='utf-8') 
file2.write(final)