file= open("c1.txt",'r')
wordcount = dict()
for line in file:
    words= line.strip().split(" ")
    for word in words:
        if word in wordcount:
            wordcount[word]=wordcount[word]+1
        else:
            wordcount[word]=1

for key in list(wordcount.keys()):
    print(key,wordcount[key])

filew= open("c1.txt",'w')
filew.write(str(wordcount))