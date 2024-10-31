

lst= [0,7,2,8,5,3,10]


def od(l):
    odd = 0
    for i in range(len(l)):
      if l[i] % 2 == 1:
          odd = i + 1
        
    return odd 
        

print(od(lst))


