def whatFlavors(cost, money):
    index1=0
    index2=0
    i=0
    m={}
    for ele in cost:
        try:
            m[ele]=m[ele]+1
        except:
            m[ele]=1
    for ele in cost:
        index1=ele;
        try:
           if(m[money-index1]>=1):
               flag=1
               if(money-index1==index1):
                    flag=0
                    if(m[money-index1]>1):
                        flag=1
               if(flag==1):
                index2=money-index1
                break;
        except:
            continue



    index1=cost.index(index1)

    cost[index1]=0
    index2=cost.index(index2)




    if(index1>index2):
        print(index2+1,end=' ')
        print(index1+1,end=' ')
    else:
        print(index1+1,end=' ')
        print(index2+1,end=' ')
    print()
