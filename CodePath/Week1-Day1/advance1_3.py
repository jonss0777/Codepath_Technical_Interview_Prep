
'''
Problem: 
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy()
that accepts a string word and returns a new string that removes any
substrings t, i, gg, and er from word. The function should be case
insensitive.



Understand: 
Removing substring 
t , i, gg , er, from word 

Plan:

- have a variable that matches the previous word and see if it matches g or e 

- make word word into a list 

t= set('t', 'gg', 'i', 'er')

for in range()
    that jumps by 1, 2 elements 
    
    if < looking ahead: i+1 < len(word)
    
Implement :

'''


def tiggerfy(word):

    t = set(['t', 'gg', 'i', 'er'])

    indexes = []
    n = len(word)
    for i in range(n):
        # 1 element
        if word[i].lower() in t:
            indexes.append(i)
        elif i+1 < n and word[i:i+2] in t:
            indexes.append(i)
            indexes.append(i+1)
               
    result = ""
    for i in range(n):
        if i not in indexes:
            result += word[i]
                
    return result
        
        
word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))










