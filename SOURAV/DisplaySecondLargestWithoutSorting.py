def display_second_largest(a):
    l = max(a)
    cpy = []
    for e in a:
        if e != l:
            cpy.append(e)
    
    print(max(cpy))

display_second_largest([3,56,2,5,4,5,3,6,8,31,5,4,2,1,3,42,56])