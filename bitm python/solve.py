def problem(str):
    str_vlu=""
    for b in str:
        if ((b >= 'A' and b <= 'Z') or
            (b >= 'a' and b <= 'z')): 
            str_vlu=str_vlu+b
    # slicing the string in reverse fashion  
    reverse_str=""
    for element in str_vlu[ : :-1]: 
       reverse_str+=element 
    return reverse_str 
    print('\n') 
print(problem("d89%l++5r19o7W *o=l645le9H"))
