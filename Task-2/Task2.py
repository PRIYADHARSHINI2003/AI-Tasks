from os import read


with open("F1.txt",'r') as F1:
    with open("F2.txt",'r') as F2:
        with open("F3.txt",'w') as F3:
            file1 = F1.read()
            file2 = F2.read()
            
            i=j=0
            while i < len(file1) or j < len(file2):
                word1 = ""
                word2 = ""
                if i < len(file1):
                    while file1[i] != ' ' and file1[i] != '':
                        word1 += file1[i]
                        i+=1
                        if  i >= len(file1):
                            break
                    F3.write(word1 + ' ')    
                if j < len(file2):
                    while file2[j] != ' ' and file2[j] != '':
                        word2 += file2[j]
                        j+=1
                        if  j >= len(file2):
                            break
                    F3.write(word2 + ' ')
                i+=1
                j+=1
