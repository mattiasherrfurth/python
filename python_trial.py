def min(lst):
    return sorted(lst)[0]

def max(lst):
    return sorted(lst)[-1]

def median(lst):
    return sorted(lst)[round(len(lst)/2)-1]

def quartone(lst):
    return sorted(lst)[round(len(lst)/4)]

def quartthree(lst):
    return sorted(lst)[3*round(len(lst)/4)]
    
    
dum = [4, 1, 6, 3, 39, 5, 2]

print('min =', sorted(dum))
print(min(dum))
print(max(dum))
print(median(dum))
print(quartone(dum))
print(quartthree(dum))
