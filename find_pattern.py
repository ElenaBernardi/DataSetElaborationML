from collections import defaultdict

'''metodo che trova i pattern ricorrenti in una lista, e ritorna in output la lista dei pattern trovati'''
def get_patters(A, B, window):
    d = defaultdict(int)
    #while(len(B)>1):
    while(len(B)>=window):
        C = []
        B.pop(0)
        for i in range(len(B)):
            C.append(A[i] == B[i])
        list = find_pattern(C, A, window)
        for k in list:
           d[k] = d[k]+1
    return d

def find_pattern(C,A,window):
    count=0
    list=[]
    for i in range(0,len(C)):
        if(C[i]):
            count = count+1
        else:
            count=0
        if(count==window):
            list.append(get_list(A,window,i))
            count = count-1
    return list

def get_list(A,window,i):

    str = ""
    for j in range(0,window):
        str = A[i]+" "+str
        i = i-1
    return str
