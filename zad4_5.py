def odwracanie(L, left, right):
    
    if left >= len(L) or  right >= len(L):
        return -1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left, right = left + 1, right - 1
    
    return L

def odwracanier(L,left,right):
    if left >= len(L) or  right >= len(L):
        return -1
    
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanier(L,left+1,right-1)
    
    return L


L= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
left=0
right =9
print(odwracanier(L,left,right))