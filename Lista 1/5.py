def example(*lista):
    new_list = []
    ma = max(lista)
    mi = min(lista)
    factor = max(abs(mi), abs(ma))
    print "The factor is:",factor
    for i in range(0, len(lista)):
        new_list.append(lista[i] / float(factor))
        i += 1        
    print "The new list is:", new_list


example(1, 4, -10, 3, 2)
