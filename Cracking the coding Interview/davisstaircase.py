ma={}
def stepPerms(n):
    global ma;
    if(n==0):
        return 1;
    if(n>0):
        try:
            if(ma[n]):
                pass
        except:

                cnt=stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3);
                ma[n]=cnt
        return ma[n]
    if(n<0):
        return 0;
