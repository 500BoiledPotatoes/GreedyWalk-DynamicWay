with open("dynamicway.rt","w") as allways:#create an RT file
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
    path=[[0 for i in range(len(map))]for j in range(len(map))]
    coordinate=[[0 for i in range(len(map))]for j in range(len(map)-1)]
    print(len(coordinate))
    print(len(map))
    j=0
    i=rows-1
    while i>0:
        #print(j)
        j=0
        while j<cols:
            if j==0:
        #print(i)
                if abs(map[i-1][j]-map[i][j])+path[i][j]<abs(map[i-1][j]-map[i][j+1])+path[i][j+1]:
                    path[i-1][j]=abs(map[i-1][j]-map[i][j])+path[i][j]
                    #print(abs(map[i-1][j]-map[i][j]))
                    #print(b)
                    #print(path)
                    coordinate[i-1][j]=j
                elif abs(map[i-1][j]-map[i][j])+path[i][j]>abs(map[i-1][j]-map[i][j+1])+path[i][j+1]:
                    path[i-1][j]=abs(map[i-1][j]-map[i][j+1])+path[i][j+1]
                    coordinate[i-1][j]=j+1
                elif abs(map[i-1][j]-map[i][j])+path[i][j]==abs(map[i-1][j]-map[i][j+1])+path[i][j+1]:
                    path[i-1][j]=abs(map[i-1][j]-map[i][j])+path[i][j]
                    coordinate[i-1][j]=j
            #print(path)
            if j!=0 and j!=cols-1:
                #print(i)
                #print(path)
                if abs(map[i-1][j]-map[i][j])+path[i][j]<abs(map[i-1][j]-map[i][j+1])+path[i][j+1] and abs(map[i-1][j]-map[i][j])+path[i][j]<abs(map[i-1][j]-map[i][j-1])+path[i][j-1]:
                    path[i-1][j]=abs(map[i-1][j]-map[i][j])+path[i][j]
                    coordinate[i-1][j]=j
                elif abs(map[i-1][j]-map[i][j-1])+path[i][j-1]<abs(map[i-1][j]-map[i][j])+path[i][j] and abs(map[i-1][j]-map[i][j-1])+path[i][j-1]<abs(map[i-1][j]-map[i][j+1])+path[i][j+1]:
                    path[i-1][j]=abs(map[i-1][j]-map[i][j-1])+path[i][j-1]
                    coordinate[i-1][j]=j-1
                elif  abs(map[i-1][j]-map[i][j+1])+path[i][j+1]<abs(map[i-1][j]-map[i][j])+path[i][j] and abs(map[i-1][j]-map[i][j+1])+path[i][j+1]<abs(map[i-1][j]-map[i][j-1])+path[i][j-1]:
                    path[i-1][j]=abs(map[i-1][j]-map[i][j+1])+path[i][j+1]
                    coordinate[i-1][j]=j+1
                elif abs(map[i-1][j]-map[i][j])+path[i][j]==abs(map[i-1][j]-map[i][j-1])+path[i][j-1] and abs(map[i-1][j]-map[i][j])+path[i][j]<abs(map[i-1][j]-map[i][j+1])+path[i][j+1]:
                    path[i-1][j]=abs(map[i-1][j]-map[i][j])+path[i][j]
                    coordinate[i-1][j]=j
                elif abs(map[i-1][j]-map[i][j])+path[i][j]==abs(map[i-1][j]-map[i][j+1])+path[i][j+1] and abs(map[i-1][j]-map[i][j])+path[i][j]<abs(map[i-1][j]-map[i][j-1])+path[i][j-1]:
                    path[i-1][j]=abs(map[i-1][j]-map[i][j])+path[i][j]
                    coordinate[i-1][j]=j
                elif abs(map[i-1][j]-map[i][j])+path[i][j]==abs(map[i-1][j]-map[i][j+1])+path[i][j+1]==abs(map[i-1][j]-map[i][j-1])+path[i][j-1]:
                    path[i-1][j]=abs(map[i-1][j]-map[i][j])+path[i][j]
                    coordinate[i-1][j]=j
                elif abs(map[i-1][j]-map[i][j+1])+path[i][j+1]==abs(map[i-1][j]-map[i][j-1])+path[i][j-1] and abs(map[i-1][j]-map[i][j+1])+path[i][j+1]<abs(map[i-1][j]-map[i][j])+path[i][j]:
                    import random
                    choice = random . choice ( ( True , False ) )
                    if choice == True :
                        path[i-1][j]=abs(map[i-1][j]-map[i][j+1])+path[i][j+1]
                        coordinate[i-1][j]=j+1
                    else:
                        path[i-1][j]=abs(map[i-1][j]-map[i][j-1])+path[i][j-1]
                        coordinate[i-1][j]=j-1
            if j==cols-1:
            #print(i)
                if abs(map[i-1][j]-map[i][j])+path[i][j]>abs(map[i-1][j]-map[i][j-1])+path[i][j-1]:
                    path[i-1][j]=abs(map[i-1][j]-map[i][j-1])+path[i][j-1]
                    coordinate[i-1][j]=j-1
                elif abs(map[i-1][j]-map[i][j])+path[i][j]<abs(map[i-1][j]-map[i][j-1])+path[i][j-1]:
                     path[i-1][j]=abs(map[i-1][j]-map[i][j])+path[i][j]
                     coordinate[i-1][j]=j
                elif abs(map[i-1][j]-map[i][j])+path[i][j]==abs(map[i-1][j]-map[i][j-1])+path[i][j-1]:
                    path[i-1][j]=abs(map[i-1][j]-map[i][j])+path[i][j]
                    coordinate[i-1][j]=j
            j+=1
        i=i-1
    print(path)
    print(coordinate)
    result=path[0]
    min=min(result)
    place=result.index(min)

    answer=str(min)+" "+str(place)+" "
    for k in range(rows-1):
        answer=answer+str(coordinate[k][place])+" "
        place=coordinate[k][place]
    print(answer)
        
