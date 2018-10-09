def ans(nu):
    string=str(nu)
    num=0
    for ele in string:
        num=num+ int(ele);
    if(len(str(num))==1):
        return num;
    else:
        return ans(num);


def superDigit(n, k):
    i=0
    nu=0
    for ele in n:
        nu=nu+int(ele);
    return ans(nu*k);
