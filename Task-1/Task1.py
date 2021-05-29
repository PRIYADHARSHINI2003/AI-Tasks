file = input("Enter the filename:") 
h = open(file, 'r')
 
content = h.readlines()

  
list = []
for i in range(len(content)):
    word = ""
    j=0
    while content[i][j] !='\n':
        word += content[i][j]
        j+=1
        if j == len(content[i]):
            break
    list.append(float(word)) 
Minimum = list[0]
Maximum = list[0]
sum= 0
for i in range(len(list)):
    if(list[i]>Maximum):
        Maximum = list[i]
    elif(list[i]<Minimum):
        Minimum = list[i]

    sum += list[i]
    length = len(list)
print("Minimum: " + str(Minimum))
print("Maximum: " + str(Maximum))
print("Average: " + str(sum/length))
