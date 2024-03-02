from random import *
def main():
    l=1
    while l<=10:
        l=l+1
        x=randint(1,100)
        y=randint(1,100)
        z=randint(1,100)
        print (f'{x} or {y} or {z}')        
        if x<y and x<z and y<z:
            print (x ,y ,z)
        if x<y and x<z and z<y:
            print (x ,z ,y)    
        if y<x and y<z and x<z:
            print (y ,x ,z)                
        if y<x and y<z and z<x:
            print (y ,z ,x)    
        if z<x and z<y and x<y:
            print (z ,x ,y)    
        if z<x and z<y and y<x:
            print (z ,y ,x)
        
           
main()            
