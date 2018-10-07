def pairs(k, arr):
    ma={}
    count=0
    for ele in arr:
        ma[ele]=1
    for ele in arr:
        i=ele+k
        try:
           if(ma[i]==1):
            count=count+1
        except:
            continue;
    return count;
