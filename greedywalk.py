with open("greedyway.rt","w") as allways:#create an RT file
    list2=[]
    var1=0
    var2=0
    map=[]
    list3=[]
    file=input("You should input a filename here.")
    with open(file,"r") as sample:#Read map file
        lines=sample.read()
        sample1=lines.split(" ")
        sample1="\n".join(sample1)
        list2=sample1.split("\n")#Convert the file to a list
        rows=int((list2[0]))
        cols=int((list2[1]))
        list2.remove(list2[1])
        list2.remove(list2[0])#Extract the number of rows and columns in the list
        while var1<rows*cols:
            num=int(list2[var1])
            list3.append(num)
            var1+=1
        while var2<len(list2):
            list3.append(list(list2[var2:var2+100]))
            var2+=100    
        list3.remove(list3[len(list3)-1])
        step = rows
        list4= [list3[var:var+step] for var in range(0,len(list3),step)]
        for var3 in list4:
            map.append(var3)#Turns the list into a 2D list
    print(map)
    print(len(map))
    import random
    path=[]
    coordinate=[]
    j=0
    k=0
    while k<cols:#Here are the steps of the greedy algorithm
        i=0
        j=k
        path.append(map[0][j])
        coordinate.append(j)
        while i<rows-1:
            a=map[i][j]
            b=map[i+1][j]
            d=map[i+1][j-1]
            if j==0:#In the first column
                if abs(b-a)>abs(map[i+1][j+1]-a):
                    path.append(map[i+1][j+1])
                    coordinate.append(j+1)
                    j+=1
                elif abs(b-a)<abs(map[i+1][j+1]-a):
                    path.append(b)
                    coordinate.append(j)
                    j=j
                elif abs(b-a)==abs(map[i+1][j+1]-a):
                    path.append(b)
                    coordinate.append(j)
                    j=j
            elif j==rows-1:#In the last column
                if abs(b-a)>abs(d-a):
                    path.append(d)
                    coordinate.append(j-1)
                    j=j-1
                elif abs(b-a)<abs(d-a):
                    path.append(b)
                    coordinate.append(j)
                    j=j
                elif abs(b-a)==abs(d-a):
                    path.append(b)
                    coordinate.append(j)
                    j=j
            elif j!=0 and j<cols-1:#In the other columns
                if abs(b-a)<abs(map[i+1][j+1]-a) and abs(b-a)<abs(d-a):
                    path.append(b)
                    coordinate.append(j)
                    j=j
                elif abs(map[i+1][j+1]-a)<abs(b-a) and abs(map[i+1][j+1]-a)<abs(d-a):
                    path.append(map[i+1][j+1])
                    coordinate.append(j+1)
                    j=j+1
                elif  abs(d-a)<abs(map[i+1][j+1]-a) and abs(d-a)<abs(b-a):
                    path.append(d)
                    coordinate.append(j-1)
                    j=j-1
                elif abs(b-a)==abs(map[i+1][j+1]-a) and abs(b-a)<abs(d-a):
                    path.append(b)
                    coordinate.append(j)
                    j=j
                elif abs(b-a)==abs(d-a) and abs(b-a)<abs(map[i+1][j+1]-a):
                    path.append(b)
                    coordinate.append(j)
                    j=j
                elif abs(b-a)==abs(d-a)==abs(map[i+1][j+1]-a):
                    path.append(b)
                    coordinate.append(j)
                    j=j
                elif abs(map[i+1][j+1]-a)==abs(d-a) and abs(map[i+1][j+1]-a)<abs(b-a):#If the left and right path lengths are the same, they are randomly selected
                    choice = random . choice ( ( True , False ) )
                    if choice == True :
                        path.append(map[i+1][j+1])
                        coordinate.append(j+1)
                        j=j+1
                    else:
                        path.append(d)
                        coordinate.append(j)
                        j=j-1
            i+=1
        k+=1
    x=[]
    ele=[]
    total=[]
    step = rows
    b = [path[p:p+step] for p in range(0,len(path),step)]#Extract each path from the list
    for e in b:
        for z in range(0,cols-1):
                v=abs(e[z+1]-e[z])
                ele.append(v)#Calculate each elevation change
    step =rows-1
    u = [ele[n:n+step] for n in range(0,len(ele),step)]
    step = rows-1
    u = [ele[n:n+step] for n in range(0,len(ele),step)]
    for t in u:
        total.append([sum(t)])#The total elevation change of each path
    step = rows
    m = [coordinate[l:l+step] for l in range(0,len(coordinate),step)]
    for d in m:
        x.append(d)#Find the x-coordinate for each of these paths
    w=0
    z=0
    list4=[]
    list5=[]
    while z<rows:
        list4.append(total[z])
        list4.append(x[z])
        z+=1
    while w<len(list4):
        if w%2==0:
            list5.append(list4[w][0])
        g=0
        while g<rows:
            if w%2==0:
                list5.append(list4[w+1][g])#integrate the change in elevation  with the x-coordinate
            g+=1
        w+=1
    step = int((rows*rows+rows)/rows)
    list6= [list5[o:o+step] for o in range(0,len(list5),step)]
    answer=[]
    for y in list6:
        answer.append(y)
    num=0
    while num<rows:
        allways.write(" ".join('%s' %id for id in answer[num])+"\n")#Output the result in the correct form
        num+=1


