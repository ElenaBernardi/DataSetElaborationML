from math import sqrt, pow

#metodo che restituisce il modulo del vettore di 4 elementi in ingresso (x1,y1,x2,y2)
def get_module(vector):
    cateto1=vector[2]-vector[0]
    cateto2=vector[3]-vector[1]
    module = sqrt(pow(cateto1,2)+pow(cateto2,2))
    return module

#metodo che restituisce il coefficiente angolare del vettore di 4 elementi in ingresso (x1,y1,x2,y2)
def get_gradient(vector):
    cateto1 = vector[2] - vector[0]
    cateto2 = vector[3] - vector[1]
    gradient = float(cateto2/cateto1)
    #if gradient<0:
    #    normalized = (gradient-0)/(1-0)
    return gradient

def tuple_module_gradient(vector):
    return (get_module(vector), get_gradient(vector))