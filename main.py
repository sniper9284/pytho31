fileRead = open('111.txt')
reader = fileRead.read()
reader = reader.replace("\n", "")
list = reader.split(" ")

print(list)
result = []
for i in list:
    if len(i) >= 7:
        result.append(i)
final = '\n'.join(result)
fileRead.close()
file2 = open("333.txt", "w", encoding='utf-8') 
file2.write(final)
file2.close()